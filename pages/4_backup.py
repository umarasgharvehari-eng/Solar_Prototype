import streamlit as st
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar, render_page_header

st.set_page_config(page_title="Backup", page_icon="🔋", layout="wide")
initialize_state()
inject_global_css()

render_sidebar(st.session_state.profile, st.session_state.results)
render_page_header("🔋 Backup Settings", "Set required backup time for critical appliances.")

st.markdown('<div class="page-card">', unsafe_allow_html=True)

backup_hours = st.slider(
    "Required Backup Hours",
    min_value=0,
    max_value=12,
    value=int(st.session_state.get("backup_hours", 0))
)

st.session_state.backup_hours = backup_hours
st.success(f"Backup hours saved: {backup_hours}")

st.markdown("</div>", unsafe_allow_html=True)
