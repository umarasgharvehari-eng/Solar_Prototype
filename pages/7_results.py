import streamlit as st
from core.calculations import calculate_load, solar_size, battery_size, system_cost

st.title("Results")

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
