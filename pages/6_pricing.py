import streamlit as st
from utils.session import initialize_state

initialize_state()

st.title("Pricing")

panel_price = st.number_input("Panel price per watt", min_value=1, value=35)
battery_price = st.number_input("Battery price per kWh", min_value=1, value=50000)
inverter_price = st.number_input("Inverter price", min_value=1, value=200000)
installation_cost = st.number_input("Installation cost", min_value=0, value=50000)

if st.button("Save Pricing"):
    st.session_state.pricing = {
        "panel": panel_price,
        "battery_per_kwh": battery_price,
        "inverter": inverter_price,
        "installation": installation_cost,
    }
    st.success("Pricing saved successfully")
