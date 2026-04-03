import streamlit as st
import pandas as pd
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar, render_page_header

st.set_page_config(page_title="Appliances", page_icon="🔌", layout="wide")
initialize_state()
inject_global_css()

render_sidebar(st.session_state.profile, st.session_state.results)
render_page_header("🔌 Appliances", "Add home appliances with wattage, quantity, and daily usage hours.")

preset = st.selectbox(
    "Quick Appliance Preset",
    ["Custom", "Fan", "LED Light", "Fridge", "TV", "Router", "1 Ton AC", "1.5 Ton AC", "Washing Machine", "Water Pump"]
)

preset_map = {
    "Custom": 100,
    "Fan": 80,
    "LED Light": 12,
    "Fridge": 180,
    "TV": 100,
    "Router": 15,
    "1 Ton AC": 1200,
    "1.5 Ton AC": 1700,
    "Washing Machine": 500,
    "Water Pump": 750,
}

st.markdown('<div class="page-card">', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    name = st.text_input("Appliance Name", value="" if preset == "Custom" else preset)
    watts = st.number_input("Watts", min_value=1, value=preset_map[preset])
    qty = st.number_input("Quantity", min_value=1, value=1)
with c2:
    hours = st.number_input("Hours/Day", min_value=1, max_value=24, value=4)
    on_solar = st.checkbox("Include in Solar", value=True)
    backup_required = st.checkbox("Required in Backup", value=False)

if st.button("Add Appliance"):
    st.session_state.appliances.append({
        "name": name,
        "watts": watts,
        "qty": qty,
        "hours": hours,
        "on_solar": on_solar,
        "backup_required": backup_required,
    })
    st.success(f"{name} added successfully.")

st.markdown("</div>", unsafe_allow_html=True)

if st.session_state.appliances:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.subheader("Added Appliances")
    df = pd.DataFrame(st.session_state.appliances)
    st.dataframe(df, use_container_width=True)
    if st.button("Clear All Appliances"):
        st.session_state.appliances = []
        st.success("All appliances cleared.")
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("No appliances added yet.")
