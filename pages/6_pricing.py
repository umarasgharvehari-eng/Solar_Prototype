import streamlit as st

st.title("Pricing")

price = st.number_input("Panel price per watt", 35)

st.session_state.pricing["panel"] = price
