import streamlit as st
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar, render_page_header

st.set_page_config(page_title="Customer Profile", page_icon="👤", layout="wide")

initialize_state()
inject_global_css()
render_sidebar(st.session_state.profile, st.session_state.results)
render_page_header("👤 Customer Profile", "Create, edit, and update customer details here.")

cities = ["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Faisalabad", "Multan", "Peshawar", "Quetta"]
utilities = ["LESCO", "K-Electric", "IESCO", "FESCO", "MEPCO", "GEPCO", "PESCO", "HESCO", "QESCO"]
system_types = ["On-Grid", "Hybrid", "Off-Grid"]

profile = st.session_state.get("profile", {})

city_index = cities.index(profile["city"]) if profile.get("city") in cities else 0
utility_index = utilities.index(profile["utility"]) if profile.get("utility") in utilities else 0
system_index = system_types.index(profile["system_type"]) if profile.get("system_type") in system_types else 0

st.markdown('<div class="page-card">', unsafe_allow_html=True)

with st.form("profile_form", clear_on_submit=False):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Customer Name", value=profile.get("name", ""))
        mobile = st.text_input("Mobile Number", value=profile.get("mobile", ""), placeholder="03XX1234567")
        city = st.selectbox("City", cities, index=city_index)

    with col2:
        system_type = st.selectbox("System Type", system_types, index=system_index)
        sanctioned_load = st.number_input(
            "Sanctioned Load (kW)",
            min_value=0.0,
            value=float(profile.get("sanctioned_load", 5.0)),
            step=0.5
        )
        monthly_bill = st.number_input(
            "Monthly Bill (PKR)",
            min_value=0,
            value=int(profile.get("monthly_bill", 15000)),
            step=1000
        )

    utility = st.selectbox("Utility", utilities, index=utility_index)

    c1, c2 = st.columns(2)
    with c1:
        save_clicked = st.form_submit_button("Save / Update Profile")
    with c2:
        reset_clicked = st.form_submit_button("Reset Profile")

if save_clicked:
    st.session_state.profile = {
        "name": name.strip(),
        "mobile": mobile.strip(),
        "city": city,
        "utility": utility,
        "system_type": system_type,
        "sanctioned_load": float(sanctioned_load),
        "monthly_bill": int(monthly_bill),
    }
    st.success("Profile updated successfully.")
    st.rerun()

if reset_clicked:
    st.session_state.profile = {
        "name": "",
        "mobile": "",
        "city": "",
        "utility": "",
        "system_type": "On-Grid",
        "sanctioned_load": 5.0,
        "monthly_bill": 15000,
    }
    st.success("Profile reset successfully.")
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

current = st.session_state.profile
st.markdown('<div class="page-card">', unsafe_allow_html=True)
st.subheader("Saved Profile Preview")

p1, p2, p3 = st.columns(3)
with p1:
    st.write(f"**Name:** {current.get('name', 'Not set') or 'Not set'}")
    st.write(f"**Mobile:** {current.get('mobile', 'Not set') or 'Not set'}")
with p2:
    st.write(f"**City:** {current.get('city', 'Not set') or 'Not set'}")
    st.write(f"**Utility:** {current.get('utility', 'Not set') or 'Not set'}")
with p3:
    st.write(f"**System Type:** {current.get('system_type', 'Not set') or 'Not set'}")
    st.write(f"**Monthly Bill:** PKR {int(current.get('monthly_bill', 0) or 0):,}")

st.markdown("</div>", unsafe_allow_html=True)
