import streamlit as st
from core.calculations import calculate_load, solar_size, battery_size, system_cost

st.title("Results")
st.markdown("""
<div style="
background: linear-gradient(90deg, rgba(37,99,235,0.12), rgba(16,185,129,0.12));
padding: 14px 18px;
border-radius: 16px;
margin-bottom: 16px;
border: 1px solid rgba(37,99,235,0.18);
">
<b>Tip:</b> Fields save karne ke baad next page par jao.
</div>
""", unsafe_allow_html=True)
if st.button("Calculate"):

    daily_kwh, load_watts = calculate_load(st.session_state.appliances)

    solar_kw = solar_size(daily_kwh)
    battery_kwh = battery_size(load_watts, st.session_state.backup_hours)
    cost = system_cost(solar_kw, battery_kwh)

    st.session_state.results = {
        "solar_size_kw": solar_kw,
        "battery_kwh": battery_kwh,
        "total_cost": cost
    }

    st.success("Calculated")

st.write(st.session_state.get("results", {}))
