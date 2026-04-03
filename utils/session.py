import streamlit as st


def initialize_state():
    defaults = {
        "profile": {
            "name": "",
            "phone": "",
            "city": "Lahore",
            "utility": "LESCO",
            "connection_type": "Single Phase",
            "system_type": "Hybrid",
            "sanctioned_load_kw": 5.0,
            "monthly_bill_pkr": 25000,
            "monthly_units_kwh": 450,
        },
        "appliances": [],
        "backup_hours": 4,
        "backup_type": "Lithium",
        "roof": {
            "area_sqft": 500,
            "shading": "Low",
            "roof_type": "RCC",
        },
        "pricing": {
            "panel_price_per_watt": 34.0,
            "inverter_cost": 260000.0,
            "battery_price_per_kwh": 95000.0,
            "structure_cost": 85000.0,
            "bos_cost": 55000.0,
            "labor_cost": 65000.0,
            "transport_cost": 20000.0,
            "documentation_cost": 30000.0,
            "contingency_percent": 5.0,
            "import_tariff": 65.0,
            "export_tariff": 21.0,
        },
        "results": {},
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
