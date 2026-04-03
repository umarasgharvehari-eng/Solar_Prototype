import streamlit as st

st.title("Roof")

area = st.number_input("Roof area (sq ft)", 0)

st.session_state.roof = area
