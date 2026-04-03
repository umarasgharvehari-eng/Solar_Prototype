import streamlit as st

def initialize_state():
    if "profile" not in st.session_state:
        st.session_state.profile = {}

    if "appliances" not in st.session_state:
        st.session_state.appliances = []

    if "solar_selection" not in st.session_state:
        st.session_state.solar_selection = []

    if "backup_hours" not in st.session_state:
        st.session_state.backup_hours = 0

    if "roof" not in st.session_state:
        st.session_state.roof = 0

    if "pricing" not in st.session_state:
        st.session_state.pricing = {}

    if "results" not in st.session_state:
        st.session_state.results = {}
