import streamlit as st
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar_summary, top_hero

st.set_page_config(
    page_title="Pakistan Solar Panel Requirement System",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_state()
inject_global_css()
render_sidebar_summary()

top_hero(
    title="Pakistan Solar Panel Requirement System",
    subtitle="Professional solar sizing, backup planning, costing, savings, and PDF quotation for Pakistan local customers.",
)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """
        <div class='metric-card'>
            <div class='metric-title'>What this app does</div>
            <ul>
              <li>Collects customer and utility details</li>
              <li>Captures appliance load and usage</li>
              <li>Calculates solar, inverter, and battery requirement</li>
              <li>Estimates cost, savings, and payback</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class='metric-card'>
            <div class='metric-title'>Recommended Flow</div>
            <ol>
              <li>Customer Profile</li>
              <li>Appliances</li>
              <li>Solar Selection</li>
              <li>Backup</li>
              <li>Roof</li>
              <li>Pricing</li>
              <li>Results</li>
              <li>Export PDF</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class='metric-card'>
            <div class='metric-title'>Pakistan Focus</div>
            <ul>
              <li>PKR costing</li>
              <li>City-based sun hours</li>
              <li>On-grid / Hybrid / Off-grid</li>
              <li>Household backup planning</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.info("Open the numbered pages from the sidebar to complete the quotation flow.")
