import streamlit as st
from utils.session import initialize_state

initialize_state()

st.title("🔌 Appliances")

st.markdown("""
<div style="
background: white;
padding: 20px;
border-radius: 20px;
box-shadow: 0 8px 24px rgba(15,23,42,0.08);
border: 1px solid #e2e8f0;
margin-bottom: 18px;">
Add home appliances with wattage, quantity, and daily usage hours.
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    name = st.text_input("Appliance Name")
with col2:
    watts = st.number_input("Watts", min_value=1, value=100)
with col3:
    qty = st.number_input("Quantity", min_value=1, value=1)
with col4:
    hours = st.number_input("Hours/Day", min_value=1, max_value=24, value=4)

if st.button("Add Appliance"):
    st.session_state.appliances.append({
        "name": name,
        "watts": watts,
        "qty": qty,
        "hours": hours
    })
    st.success(f"{name} added successfully.")

if st.session_state.appliances:
    st.subheader("Added Appliances")
    st.dataframe(st.session_state.appliances, use_container_width=True)
else:
    st.info("No appliances added yet.")
