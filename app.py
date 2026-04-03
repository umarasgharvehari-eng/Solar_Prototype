import streamlit as st

def inject_global_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #eef4ff 0%, #edfdf7 100%);
    }

    .block-container {
        max-width: 1200px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #08152f 0%, #12285f 55%, #1f3d8a 100%);
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .hero-card {
        background: linear-gradient(135deg, #2563eb 0%, #06b6d4 55%, #10b981 100%);
        padding: 26px 28px;
        border-radius: 28px;
        color: white;
        box-shadow: 0 16px 40px rgba(37, 99, 235, 0.22);
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 2.25rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 6px;
    }

    .hero-subtitle {
        font-size: 1rem;
        opacity: 0.95;
    }

    .page-card {
        background: rgba(255,255,255,0.92);
        padding: 22px;
        border-radius: 24px;
        border: 1px solid rgba(226,232,240,0.95);
        box-shadow: 0 10px 28px rgba(15,23,42,0.07);
        margin-bottom: 18px;
    }

    .metric-card {
        background: white;
        border-radius: 22px;
        padding: 18px 20px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        border: 1px solid rgba(226, 232, 240, 0.95);
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

    .section-title {
        font-size: 1.85rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 10px;
    }

    .note-box {
        background: linear-gradient(90deg, rgba(37,99,235,0.10), rgba(16,185,129,0.10));
        border: 1px solid rgba(37,99,235,0.18);
        padding: 15px 17px;
        border-radius: 16px;
        color: #0f172a;
        font-weight: 500;
    }

    .profile-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 14px;
        margin-top: 10px;
    }

    .mini-card {
        background: white;
        border-radius: 18px;
        padding: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 6px 18px rgba(15,23,42,0.05);
    }

    .mini-label {
        color: #64748b;
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 6px;
    }

    .mini-value {
        color: #0f172a;
        font-size: 1.02rem;
        font-weight: 800;
        word-break: break-word;
    }

    .stButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #10b981 100%);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 0.72rem 1.2rem;
        font-weight: 700;
        box-shadow: 0 10px 18px rgba(37, 99, 235, 0.20);
    }

    .stButton > button:hover {
        filter: brightness(1.03);
    }

    .stDownloadButton > button {
        background: linear-gradient(90deg, #2563eb 0%, #10b981 100%);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 0.72rem 1.2rem;
        font-weight: 700;
    }

    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] > div {
        border-radius: 14px !important;
    }

    @media (max-width: 900px) {
        .hero-title {
            font-size: 1.7rem;
        }
        .profile-grid {
            grid-template-columns: 1fr;
        }
        .block-container {
            padding-left: 0.8rem;
            padding-right: 0.8rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_page_header(title, subtitle):
    st.markdown(f"""
    <div class="page-card">
        <div class="section-title">{title}</div>
        <div class="note-box">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar(profile, results):
    st.sidebar.markdown("## ⚡ Quick Summary")
    st.sidebar.markdown(f"**Customer:** {profile.get('name', 'Not set') or 'Not set'}")
    st.sidebar.markdown(f"**Mobile:** {profile.get('mobile', 'Not set') or 'Not set'}")
    st.sidebar.markdown(f"**City:** {profile.get('city', 'Not set') or 'Not set'}")
    st.sidebar.markdown(f"**Utility:** {profile.get('utility', 'Not set') or 'Not set'}")
    st.sidebar.markdown(f"**System Type:** {profile.get('system_type', 'Not set') or 'Not set'}")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Solar Size:** {results.get('solar_size_kw', 0.0):.2f} kW")
    st.sidebar.markdown(f"**Battery:** {results.get('battery_kwh', 0.0):.2f} kWh")
    st.sidebar.markdown(f"**Cost:** PKR {results.get('total_cost', 0):,.0f}")
