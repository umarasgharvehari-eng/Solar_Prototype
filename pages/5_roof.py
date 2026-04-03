import streamlit as st
from utils.session import initialize_state

initialize_state()

st.title("🏠 Roof Details")

col1, col2 = st.columns(2)

with col1:
    roof_area = st.number_input(
        "Available Roof Area (sq ft)",
        min_value=0,
        value=int(st.session_state.roof.get("area_sqft", 500))
    )
with col2:
    shading = st.selectbox(
        "Shading Level",
        ["None", "Low", "Medium", "High"],
        index=["None", "Low", "Medium", "High"].index(
            st.session_state.roof.get("shading", "Low")
        )
    )

if st.button("Save Roof Details"):
    st.session_state.roof = {
        "area_sqft": roof_area,
        "shading": shading,
    }
    st.success("Roof details saved.")
