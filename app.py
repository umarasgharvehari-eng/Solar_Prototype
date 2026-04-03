import streamlit as st
from utils.session import initialize_state

st.set_page_config(
    page_title='Pakistan Solar Sizing App',
    page_icon='☀️',
    layout='wide',
    initial_sidebar_state='expanded',
)

initialize_state()

st.title('☀️ Pakistan Solar Panel Requirement System')
st.caption('Streamlit MVP for household solar sizing, backup planning, and cost estimation.')

with st.sidebar:
    st.subheader('Quick Summary')
    profile = st.session_state.get('profile', {})
    result = st.session_state.get('results', {})
    st.write(f"**Customer:** {profile.get('customer_name', 'Not set')}")
    st.write(f"**City:** {profile.get('city', 'Not set')}")
    st.write(f"**Utility:** {profile.get('utility', 'Not set')}")
    st.write(f"**System Type:** {st.session_state.get('backup', {}).get('system_type', 'Not set')}")
    st.divider()
    st.write(f"**Solar Size:** {result.get('solar_size_kw', 0):.2f} kW")
    st.write(f"**Battery:** {result.get('battery_size_kwh', 0):.2f} kWh")
    st.write(f"**Cost:** PKR {result.get('total_cost_pkr', 0):,.0f}")

st.markdown(
    '''
### What this app does
- Collects household profile and utility details
- Captures appliance loads and usage hours
- Lets the user choose which loads go to solar and backup
- Sizes solar, inverter, and battery
- Estimates monthly generation, savings, cost, and payback

### Pages
Use the left sidebar to open the numbered pages.

import streamlit as st
from utils.session import initialize_state

initialize_state()

st.set_page_config(page_title="Solar App", layout="wide")

st.sidebar.title("Quick Summary")

profile = st.session_state.get("profile", {})

st.sidebar.write(f"Customer: {profile.get('name', 'Not set')}")
st.sidebar.write(f"City: {profile.get('city', 'Not set')}")
st.sidebar.write(f"Utility: {profile.get('utility', 'Not set')}")
st.sidebar.write(f"System Type: {profile.get('system_type', 'Not set')}")

st.title("🌞 Pakistan Solar Panel Requirement System")
st.write("Use sidebar to navigate pages.")
'''
)

st.info('Recommended flow: 1) Customer Profile → 2) Appliance Input → 3) Solar Selection → 4) Backup → 5) Roof → 6) Pricing → 7) Results → 8) Export')
