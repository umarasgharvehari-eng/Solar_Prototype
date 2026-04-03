import streamlit as st
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar, render_page_header

st.set_page_config(page_title="Roof", page_icon="🏠", layout="wide")
initialize_state()
inject_global_css()

render_sidebar(st.session_state.profile, st.session_state.results)
render_page_header("🏠 Roof Details", "Enter available roof space and shading conditions.")

roof = st.session_state.roof

st.markdown('<div class="page-card">', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    roof_area = st.number_input("Available Roof Area (sq ft)", min_value=0, value=int(roof.get("area_sqft", 500)))
with c2:
    shading_options = ["None", "Low", "Medium", "High"]
    shading = st.selectbox(
        "Shading Level",
        shading_options,
        index=shading_options.index(roof.get("shading", "Low"))
    )

if st.button("Save Roof Details"):
    st.session_state.roof = {
        "area_sqft": roof_area,
        "shading": shading,
    }
    st.success("Roof details saved.")

st.markdown("</div>", unsafe_allow_html=True)
