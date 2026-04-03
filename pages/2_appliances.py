import streamlit as st

st.title("Appliances")

name = st.text_input("Appliance Name")
watts = st.number_input("Watts", 0)
qty = st.number_input("Quantity", 1)
hours = st.number_input("Hours/day", 1)

if st.button("Add"):
    st.session_state.appliances.append({
        "name": name,
        "watts": watts,
        "qty": qty,
        "hours": hours
    })

st.write(st.session_state.appliances)
