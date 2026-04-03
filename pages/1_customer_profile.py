import streamlit as st
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar

st.set_page_config(
    page_title="Pakistan Solar Panel Requirement System",
    page_icon="🌞",
    layout="wide",
    initial_sidebar_state="expanded"
)

initialize_state()
inject_global_css()

profile = st.session_state.get("profile", {})
results = st.session_state.get("results", {})

render_sidebar(profile, results)

st.markdown("""
<div class="hero-card">
    <div class="hero-title">🌞 Pakistan Solar Panel Requirement System</div>
    <div class="hero-subtitle">
        Smart solar sizing, backup planning, pricing, and quotation generation for Pakistan households.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Estimated Solar Size</div>
        <div class="metric-value">{results.get('solar_size_kw', 0.0):.2f} kW</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Battery Backup</div>
        <div class="metric-value">{results.get('battery_kwh', 0.0):.2f} kWh</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Estimated Cost</div>
        <div class="metric-value">PKR {results.get('total_cost', 0):,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="page-card">
    <div class="section-title">👤 Customer Profile Summary</div>
    <div class="profile-grid">
        <div class="mini-card">
            <div class="mini-label">Customer Name</div>
            <div class="mini-value">{}</div>
        </div>
        <div class="mini-card">
            <div class="mini-label">Mobile Number</div>
            <div class="mini-value">{}</div>
        </div>
        <div class="mini-card">
            <div class="mini-label">City</div>
            <div class="mini-value">{}</div>
        </div>
        <div class="mini-card">
            <div class="mini-label">Utility</div>
            <div class="mini-value">{}</div>
        </div>
        <div class="mini-card">
            <div class="mini-label">System Type</div>
            <div class="mini-value">{}</div>
        </div>
        <div class="mini-card">
            <div class="mini-label">Monthly Bill</div>
            <div class="mini-value">PKR {:,}</div>
        </div>
    </div>
</div>
""".format(
    profile.get("name", "Not set") or "Not set",
    profile.get("mobile", "Not set") or "Not set",
    profile.get("city", "Not set") or "Not set",
    profile.get("utility", "Not set") or "Not set",
    profile.get("system_type", "Not set") or "Not set",
    int(profile.get("monthly_bill", 0) or 0),
), unsafe_allow_html=True)

st.markdown("""
<div class="page-card">
    <div class="section-title">🚀 Recommended Workflow</div>
    <div class="note-box">
        1) Customer Profile → 2) Appliances → 3) Solar Selection → 4) Backup → 5) Roof → 6) Pricing → 7) Results → 8) Export PDF
    </div>
</div>
""", unsafe_allow_html=True)
