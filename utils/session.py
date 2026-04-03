import streamlit as st

def initialize_state():
    defaults = {
        "profile": {
            "name": "",
            "mobile": "",
            "city": "",
            "utility": "",
            "system_type": "On-Grid",
            "sanctioned_load": 5.0,
            "monthly_bill": 15000,
        },
        "appliances": [],
        "solar_selection": [],
        "backup_hours": 0,
        "roof": {
            "area_sqft": 500,
            "shading": "Low",
        },
        "pricing": {
            "panel_watt": 585,
            "panel_price_per_watt": 35,
            "battery_price_per_kwh": 50000,
            "inverter_price": 250000,
            "installation_cost": 80000,
            "structure_cost": 50000,
            "bos_cost": 40000,
            "transport_cost": 15000,
        },
        "results": {},
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
