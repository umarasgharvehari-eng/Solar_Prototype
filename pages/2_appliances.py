import streamlit as st
import pandas as pd
from utils.session import initialize_state

initialize_state()

st.title("🔌 Appliances")

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

col1, col2, col3, col4 = st.columns(4)

with col1:
    name = st.text_input("Appliance Name", value="" if preset == "Custom" else preset)
with col2:
    watts = st.number_input("Watts", min_value=1, value=preset_map[preset])
with col3:
    qty = st.number_input("Quantity", min_value=1, value=1)
with col4:
    hours = st.number_input("Hours/Day", min_value=1, max_value=24, value=4)

col5, col6 = st.columns(2)
with col5:
    on_solar = st.checkbox("Include in Solar", value=True)
with col6:
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

if st.session_state.appliances:
    st.subheader("Added Appliances")
    df = pd.DataFrame(st.session_state.appliances)
    st.dataframe(df, use_container_width=True)

    if st.button("Clear All Appliances"):
        st.session_state.appliances = []
        st.success("All appliances cleared.")
else:
    st.info("No appliances added yet.")
