import streamlit as st
from utils.session import initialize_state

initialize_state()

st.title("👤 Customer Profile")

st.markdown("""
<div style="
background: white;
padding: 20px;
border-radius: 20px;
box-shadow: 0 8px 24px rgba(15,23,42,0.08);
border: 1px solid #e2e8f0;
margin-bottom: 18px;">
Fill in customer and electricity connection details.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Customer Name", value=st.session_state.profile.get("name", ""))
    city = st.selectbox(
        "City",
        ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Faisalabad", "Multan", "Peshawar", "Quetta"],
        index=0
    )
    utility = st.selectbox(
        "Utility",
        ["LESCO", "K-Electric", "IESCO", "FESCO", "MEPCO", "GEPCO", "PESCO", "HESCO", "QESCO"]
    )

with col2:
    system_type = st.selectbox("System Type", ["On-Grid", "Hybrid", "Off-Grid"])
    sanctioned_load = st.number_input("Sanctioned Load (kW)", min_value=0.0, value=5.0, step=0.5)
    monthly_bill = st.number_input("Monthly Bill (PKR)", min_value=0, value=15000, step=1000)

if st.button("Save Profile"):
    st.session_state.profile = {
        "name": name,
        "city": city,
        "utility": utility,
        "system_type": system_type,
        "sanctioned_load": sanctioned_load,
        "monthly_bill": monthly_bill
    }
    st.success("Profile saved successfully.")
