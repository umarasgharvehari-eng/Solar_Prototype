import streamlit as st

st.title("👤 Customer Profile")

name = st.text_input("Customer Name")
city = st.selectbox("City", ["Lahore", "Karachi", "Islamabad", "Faisalabad"])

utility = st.selectbox("Utility", [
    "LESCO", "K-Electric", "IESCO", "FESCO", "MEPCO"
])

connection = st.selectbox("Connection Type", ["Single Phase", "Three Phase"])

sanctioned_load = st.number_input("Sanctioned Load (kW)", min_value=0.0)

bill = st.number_input("Monthly Bill (PKR)", min_value=0)

if st.button("Save Profile"):
    st.session_state.profile = {
        "name": name,
        "city": city,
        "utility": utility,
        "connection": connection,
        "sanctioned_load": sanctioned_load,
        "bill": bill
    }
    st.success("Profile saved!")
