import streamlit as st
from utils.session import initialize_state

st.set_page_config(
    page_title="Pakistan Solar Panel Requirement System",
    page_icon="🌞",
    layout="wide",
    initial_sidebar_state="expanded"
)

initialize_state()

profile = st.session_state.get("profile", {})
results = st.session_state.get("results", {})

st.markdown("""
<style>
/* App background */
.stApp {
    background: linear-gradient(135deg, #f4f7ff 0%, #eefbf7 100%);
}

/* Main container */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e3a8a 100%);
}
[data-testid="stSidebar"] * {
    color: white !important;
}
[data-testid="stSidebar"] .stMarkdown h1,
[data-testid="stSidebar"] .stMarkdown h2,
[data-testid="stSidebar"] .stMarkdown h3 {
    color: #ffffff !important;
}

/* Header card */
.hero-card {
    background: linear-gradient(135deg, #2563eb 0%, #06b6d4 50%, #10b981 100%);
    padding: 28px 30px;
    border-radius: 24px;
    color: white;
    box-shadow: 0 14px 35px rgba(37, 99, 235, 0.25);
    margin-bottom: 20px;
}
.hero-title {
    font-size: 2.2rem;
    font-weight: 800;
    margin-bottom: 6px;
}
.hero-subtitle {
    font-size: 1rem;
    opacity: 0.95;
}

/* Summary cards */
.metric-card {
    background: white;
    border-radius: 20px;
    padding: 18px 20px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
    border: 1px solid rgba(226, 232, 240, 0.9);
    margin-bottom: 14px;
}
.metric-label {
    font-size: 0.95rem;
    color: #475569;
    margin-bottom: 8px;
    font-weight: 600;
}
.metric-value {
    font-size: 1.55rem;
    font-weight: 800;
    color: #0f172a;
}

/* Section card */
.section-card {
    background: rgba(255,255,255,0.88);
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.07);
    border: 1px solid rgba(226, 232, 240, 0.8);
    margin-top: 14px;
    margin-bottom: 18px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #2563eb 0%, #10b981 100%);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.7rem 1.2rem;
    font-weight: 700;
    box-shadow: 0 8px 18px rgba(37, 99, 235, 0.25);
}
.stButton > button:hover {
    filter: brightness(1.05);
    transform: translateY(-1px);
}

/* Inputs */
.stTextInput > div > div > input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div,
.stTextArea textarea {
    border-radius: 12px !important;
}

/* Info alert */
.custom-note {
    background: linear-gradient(90deg, rgba(37,99,235,0.12), rgba(16,185,129,0.12));
    border: 1px solid rgba(37,99,235,0.18);
    padding: 16px 18px;
    border-radius: 16px;
    color: #0f172a;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## ⚡ Quick Summary")
st.sidebar.markdown(f"**Customer:** {profile.get('name', 'Not set')}")
st.sidebar.markdown(f"**City:** {profile.get('city', 'Not set')}")
st.sidebar.markdown(f"**Utility:** {profile.get('utility', 'Not set')}")
st.sidebar.markdown(f"**System Type:** {profile.get('system_type', 'Not set')}")
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Solar Size:** {results.get('solar_size_kw', 0.0):.2f} kW")
st.sidebar.markdown(f"**Battery:** {results.get('battery_kwh', 0.0):.2f} kWh")
st.sidebar.markdown(f"**Cost:** PKR {results.get('total_cost', 0):,.0f}")

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
<div class="section-card">
    <h3 style="margin-top:0; color:#0f172a;">🚀 Recommended Workflow</h3>
    <div class="custom-note">
        1) Customer Profile → 2) Appliances → 3) Solar Selection → 4) Backup → 5) Roof → 6) Pricing → 7) Results → 8) Export PDF
    </div>
</div>
""", unsafe_allow_html=True)
