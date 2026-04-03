import streamlit as st
from utils.session import initialize_state

initialize_state()

st.title("🔋 Backup Settings")

backup_hours = st.slider(
    "Required Backup Hours",
    min_value=0,
    max_value=12,
    value=int(st.session_state.get("backup_hours", 0))
)

st.session_state.backup_hours = backup_hours

st.success(f"Backup hours saved: {backup_hours}")
