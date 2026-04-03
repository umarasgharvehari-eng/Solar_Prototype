import streamlit as st

st.title("Appliances")
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
