import streamlit as st

st.title("Customer Profile")

name = st.text_input("Name")
city = st.text_input("City")

if st.button("Save"):
    st.session_state.profile = {
        "name": name,
        "city": city
    }
    st.success("Saved")
