import streamlit as st


def inject_global_css():
    st.markdown(
        """
        <style>
        .stApp {background: linear-gradient(180deg, #f8fafc 0%, #eef6ff 100%);} 
        [data-testid="stSidebar"] {background: #0f172a;}
        [data-testid="stSidebar"] * {color: #e2e8f0;}
        .hero-box {
            background: linear-gradient(135deg, #082f49, #1d4ed8 60%, #38bdf8);
            padding: 1.4rem 1.6rem;
            border-radius: 20px;
            color: white;
            box-shadow: 0 12px 30px rgba(2, 6, 23, 0.18);
            margin-bottom: 1rem;
        }
        .hero-title {font-size: 2.1rem; font-weight: 800; margin-bottom: .35rem;}
        .hero-subtitle {font-size: 1rem; opacity: .92;}
        .metric-card {
            background: rgba(255,255,255,.92);
            border: 1px solid #dbeafe;
            border-radius: 18px;
            padding: 1rem 1rem .8rem 1rem;
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
            min-height: 220px;
        }
        .metric-title {font-size: 1.05rem; font-weight: 700; margin-bottom: .6rem; color: #0f172a;}
        .small-note {color: #475569; font-size: .92rem;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar_summary():
    profile = st.session_state.get("profile", {})
    results = st.session_state.get("results", {})
    st.sidebar.title("Quick Summary")
    st.sidebar.write(f"**Customer:** {profile.get('name') or 'Not set'}")
    st.sidebar.write(f"**City:** {profile.get('city', 'Not set')}")
    st.sidebar.write(f"**Utility:** {profile.get('utility', 'Not set')}")
    st.sidebar.write(f"**System Type:** {profile.get('system_type', 'Not set')}")
    st.sidebar.markdown("---")
    st.sidebar.write(f"**Solar Size:** {results.get('solar_size_kw', 0.0):.2f} kW")
    st.sidebar.write(f"**Battery:** {results.get('battery_kwh', 0.0):.2f} kWh")
    st.sidebar.write(f"**Inverter:** {results.get('inverter_kw', 0.0):.2f} kW")
    st.sidebar.write(f"**Cost:** PKR {results.get('total_cost', 0):,.0f}")
    st.sidebar.write(f"**Savings / Month:** PKR {results.get('monthly_savings', 0):,.0f}")


def top_hero(title: str, subtitle: str):
    st.markdown(
        f"""
        <div class='hero-box'>
            <div class='hero-title'>☀️ {title}</div>
            <div class='hero-subtitle'>{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
