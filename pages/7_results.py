import streamlit as st
import pandas as pd
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar, render_page_header
from core.calculations import (
    calculate_load,
    calculate_backup_load,
    solar_size_required,
    battery_size_required,
    panel_count_required,
    actual_panel_capacity_kw,
    estimate_monthly_generation,
    estimate_monthly_savings,
    estimate_payback_years,
    recommend_inverter_size,
    calculate_system_cost,
)

st.set_page_config(page_title="Results", page_icon="📊", layout="wide")
initialize_state()
inject_global_css()

render_sidebar(st.session_state.profile, st.session_state.results)
render_page_header("📊 Results Dashboard", "Calculate final solar size, panel count, project cost, and savings.")

if st.button("Calculate System"):
    appliances = st.session_state.appliances
    pricing = st.session_state.pricing
    roof = st.session_state.roof

    daily_kwh, connected_watts = calculate_load(appliances)
    backup_watts = calculate_backup_load(appliances)

    shading = roof.get("shading", "Low")
    performance_ratio = 0.78
    if shading == "None":
        performance_ratio = 0.80
    elif shading == "Medium":
        performance_ratio = 0.72
    elif shading == "High":
        performance_ratio = 0.65

    required_solar_kw = solar_size_required(daily_kwh, sun_hours=5.0, performance_ratio=performance_ratio)
    battery_kwh = battery_size_required(backup_watts, st.session_state.get("backup_hours", 0))
    panel_watt = pricing.get("panel_watt", 585)
    panel_count = panel_count_required(required_solar_kw, panel_watt)
    actual_solar_kw = actual_panel_capacity_kw(panel_count, panel_watt)
    inverter_kw = recommend_inverter_size(actual_solar_kw)
    monthly_generation = estimate_monthly_generation(actual_solar_kw, sun_hours=5.0, performance_ratio=performance_ratio)
    monthly_savings = estimate_monthly_savings(monthly_generation, import_tariff=65)

    costs = calculate_system_cost(
        panel_count=panel_count,
        panel_watt=panel_watt,
        panel_price_per_watt=pricing.get("panel_price_per_watt", 35),
        battery_kwh=battery_kwh,
        battery_price_per_kwh=pricing.get("battery_price_per_kwh", 50000),
        inverter_price=pricing.get("inverter_price", 250000),
        installation_cost=pricing.get("installation_cost", 80000),
        structure_cost=pricing.get("structure_cost", 50000),
        bos_cost=pricing.get("bos_cost", 40000),
        transport_cost=pricing.get("transport_cost", 15000),
    )

    roof_area = roof.get("area_sqft", 0)
    max_roof_kw = roof_area / 85 if roof_area > 0 else 0
    payback_years = estimate_payback_years(costs["total_cost"], monthly_savings)

    st.session_state.results = {
        "daily_kwh": daily_kwh,
        "connected_watts": connected_watts,
        "backup_watts": backup_watts,
        "required_solar_kw": required_solar_kw,
        "solar_size_kw": actual_solar_kw,
        "battery_kwh": battery_kwh,
        "panel_watt": panel_watt,
        "panel_count": panel_count,
        "inverter_kw": inverter_kw,
        "monthly_generation": monthly_generation,
        "monthly_savings": monthly_savings,
        "payback_years": payback_years,
        "max_roof_kw": max_roof_kw,
        "performance_ratio": performance_ratio,
        **costs,
    }

results = st.session_state.results

if results:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Daily Load", f"{results['daily_kwh']:.2f} kWh")
    c2.metric("Solar Size", f"{results['solar_size_kw']:.2f} kW")
    c3.metric("Panels", f"{results['panel_count']} x {results['panel_watt']}W")
    c4.metric("Total Cost", f"PKR {results['total_cost']:,.0f}")

    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.subheader("System Recommendation")
    st.write(f"**Recommended Solar Capacity:** {results['solar_size_kw']:.2f} kW")
    st.write(f"**Recommended Inverter:** {results['inverter_kw']} kW")
    st.write(f"**Battery Size:** {results['battery_kwh']:.2f} kWh")
    st.write(f"**Panel Wattage:** {results['panel_watt']} W")
    st.write(f"**Number of Panels:** {results['panel_count']}")
    st.write(f"**Estimated Monthly Generation:** {results['monthly_generation']:.0f} kWh")
    st.write(f"**Estimated Monthly Savings:** PKR {results['monthly_savings']:,.0f}")
    st.write(f"**Estimated Payback:** {results['payback_years']:.1f} years")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.subheader("Cost Breakdown")
    cost_df = pd.DataFrame({
        "Item": ["Solar Panels", "Battery", "Inverter", "Installation", "Structure", "BOS / Wiring", "Transport"],
        "Cost (PKR)": [
            results["panel_cost"],
            results["battery_cost"],
            results["inverter_cost"],
            results["installation_cost"],
            results["structure_cost"],
            results["bos_cost"],
            results["transport_cost"],
        ]
    })
    st.dataframe(cost_df, use_container_width=True)
    st.bar_chart(cost_df.set_index("Item"))
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("Pehle previous pages fill karo, phir Calculate System dabao.")
