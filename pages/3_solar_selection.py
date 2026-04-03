import streamlit as st
import pandas as pd
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar, render_page_header

st.set_page_config(page_title="Solar Selection", page_icon="☀️", layout="wide")
initialize_state()
inject_global_css()

render_sidebar(st.session_state.profile, st.session_state.results)
render_page_header("☀️ Solar Selection", "Choose which appliances should run on solar and which need backup.")

appliances = st.session_state.appliances

if not appliances:
    st.warning("Pehle Appliances page par appliances add karo.")
else:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.subheader("Edit Solar and Backup Selection")

    edited_rows = []
    for i, a in enumerate(appliances):
        st.markdown(f"### {a.get('name', f'Appliance {i+1}')}")
        c1, c2, c3, c4, c5, c6 = st.columns([2, 1, 1, 1, 1, 1])

        with c1:
            name = st.text_input(f"Name {i}", value=a.get("name", ""), key=f"name_{i}")
        with c2:
            watts = st.number_input(f"Watts {i}", min_value=1, value=int(a.get("watts", 100)), key=f"watts_{i}")
        with c3:
            qty = st.number_input(f"Qty {i}", min_value=1, value=int(a.get("qty", 1)), key=f"qty_{i}")
        with c4:
            hours = st.number_input(f"Hours {i}", min_value=1, max_value=24, value=int(a.get("hours", 4)), key=f"hours_{i}")
        with c5:
            on_solar = st.checkbox("Solar", value=bool(a.get("on_solar", True)), key=f"solar_{i}")
        with c6:
            backup_required = st.checkbox("Backup", value=bool(a.get("backup_required", False)), key=f"backup_{i}")

        edited_rows.append({
            "name": name,
            "watts": watts,
            "qty": qty,
            "hours": hours,
            "on_solar": on_solar,
            "backup_required": backup_required,
        })

        st.markdown("---")

    if st.button("Save Solar Selection"):
        st.session_state.appliances = edited_rows
        st.success("Solar and backup selection updated successfully.")

    st.markdown("</div>", unsafe_allow_html=True)

    df = pd.DataFrame(st.session_state.appliances)
    solar_daily_kwh = sum((a["watts"] * a["qty"] * a["hours"]) / 1000 for a in st.session_state.appliances if a.get("on_solar", True))
    backup_watts = sum((a["watts"] * a["qty"]) for a in st.session_state.appliances if a.get("backup_required", False))

    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.metric("Selected Solar Energy", f"{solar_daily_kwh:.2f} kWh/day")
    c2.metric("Backup Connected Load", f"{backup_watts:.0f} W")
    st.dataframe(df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
