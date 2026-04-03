import streamlit as st

st.title("Backup")

hours = st.slider("Backup hours", 0, 12)

st.session_state.backup_hours = hours
