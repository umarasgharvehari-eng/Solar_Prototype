import streamlit as st
from utils.session import initialize_state

initialize_state()

st.title("💰 Pricing & Components")

pricing = st.session_state.pricing

col1, col2 = st.columns(2)

with col1:
    panel_watt = st.selectbox("Panel Wattage", [545, 550, 575, 580, 585, 590, 600],
                              index=[545, 550, 575, 580, 585, 590, 600].index(pricing.get("panel_watt", 585)))
    panel_price_per_watt = st.number_input("Panel Price per Watt (PKR)", min_value=1, value=int(pricing.get("panel_price_per_watt", 35)))
    battery_price_per_kwh = st.number_input("Battery Price per kWh (PKR)", min_value=1, value=int(pricing.get("battery_price_per_kwh", 50000)))
    inverter_price = st.number_input("Inverter Price (PKR)", min_value=1, value=int(pricing.get("inverter_price", 250000)))

with col2:
    installation_cost = st.number_input("Installation Cost (PKR)", min_value=0, value=int(pricing.get("installation_cost", 80000)))
    structure_cost = st.number_input("Structure Cost (PKR)", min_value=0, value=int(pricing.get("structure_cost", 50000)))
    bos_cost = st.number_input("BOS / Wiring Cost (PKR)", min_value=0, value=int(pricing.get("bos_cost", 40000)))
    transport_cost = st.number_input("Transport Cost (PKR)", min_value=0, value=int(pricing.get("transport_cost", 15000)))

if st.button("Save Pricing"):
    st.session_state.pricing = {
        "panel_watt": panel_watt,
        "panel_price_per_watt": panel_price_per_watt,
        "battery_price_per_kwh": battery_price_per_kwh,
        "inverter_price": inverter_price,
        "installation_cost": installation_cost,
        "structure_cost": structure_cost,
        "bos_cost": bos_cost,
        "transport_cost": transport_cost,
    }
    st.success("Pricing saved successfully.")
