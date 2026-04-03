import streamlit as st

st.title("Backup")
st.markdown("""
<div style="
background: linear-gradient(90deg, rgba(37,99,235,0.12), rgba(16,185,129,0.12));
padding: 14px 18px;
border-radius: 16px;
margin-bottom: 16px;
border: 1px solid rgba(37,99,235,0.18);
">
<b>Tip:</b> Fields save karne ke baad next page par jao.
</div>
""", unsafe_allow_html=True)
hours = st.slider("Backup hours", 0, 12)

st.session_state.backup_hours = hours
