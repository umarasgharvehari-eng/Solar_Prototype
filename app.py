import streamlit as st
from utils.session import initialize_state

st.set_page_config(page_title="Solar App", layout="wide")

initialize_state()

st.sidebar.title("Quick Summary")

profile = st.session_state.get("profile", {})
results = st.session_state.get("results", {})

st.sidebar.write(f"Customer: {profile.get('name', 'Not set')}")
st.sidebar.write(f"City: {profile.get('city', 'Not set')}")
st.sidebar.write(f"Utility: {profile.get('utility', 'Not set')}")
st.sidebar.write(f"System Type: {profile.get('system_type', 'Not set')}")

st.sidebar.markdown("---")
st.sidebar.write(f"Solar Size: {results.get('solar_size_kw', 0.0):.2f} kW")
st.sidebar.write(f"Battery: {results.get('battery_kwh', 0.0):.2f} kWh")
st.sidebar.write(f"Cost: PKR {results.get('total_cost', 0):,.0f}")

st.title("🌞 Pakistan Solar Panel Requirement System")
st.write("Use the left sidebar to open the numbered pages.")

st.info(
    "Recommended flow: 1) Customer Profile → 2) Appliance Input → "
    "3) Solar Selection → 4) Backup → 5) Roof → 6) Pricing → 7) Results → 8) Export"
)
