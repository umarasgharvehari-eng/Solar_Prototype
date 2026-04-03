import streamlit as st
import pandas as pd
from core.calculations import calculate_load, solar_size, battery_size, system_cost
from utils.session import initialize_state

initialize_state()

st.title("📊 Results Dashboard")

st.markdown("""
<div style="
background: linear-gradient(90deg, rgba(37,99,235,0.12), rgba(16,185,129,0.12));
padding: 16px 18px;
border-radius: 16px;
margin-bottom: 18px;
border: 1px solid rgba(37,99,235,0.18);">
Click calculate to generate solar recommendation and cost estimate.
</div>
""", unsafe_allow_html=True)

if st.button("Calculate System"):
    daily_kwh, load_watts = calculate_load(st.session_state.appliances)
    solar_kw = solar_size(daily_kwh)
    battery_kwh = battery_size(load_watts, st.session_state.get("backup_hours", 0))
    cost = system_cost(solar_kw, battery_kwh)

    st.session_state.results = {
        "daily_kwh": daily_kwh,
        "load_watts": load_watts,
        "solar_size_kw": solar_kw,
        "battery_kwh": battery_kwh,
        "total_cost": cost
    }

results = st.session_state.get("results", {})

if results:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Daily Load", f"{results.get('daily_kwh', 0):.2f} kWh")
    c2.metric("Connected Load", f"{results.get('load_watts', 0):,.0f} W")
    c3.metric("Solar Size", f"{results.get('solar_size_kw', 0):.2f} kW")
    c4.metric("Battery", f"{results.get('battery_kwh', 0):.2f} kWh")

    st.markdown("### 💰 Cost Summary")
    st.success(f"Estimated Project Cost: PKR {results.get('total_cost', 0):,.0f}")

    if st.session_state.appliances:
        df = pd.DataFrame(st.session_state.appliances)
        st.markdown("### 📋 Appliance Table")
        st.dataframe(df, use_container_width=True)

        st.markdown("### 📈 Appliance Load Chart")
        chart_df = df.copy()
        chart_df["Total Watts"] = chart_df["watts"] * chart_df["qty"]
        st.bar_chart(chart_df.set_index("name")["Total Watts"])
else:
    st.info("No results yet. Click Calculate System.")
