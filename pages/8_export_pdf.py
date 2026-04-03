import streamlit as st
from utils.session import initialize_state
from utils.ui import inject_global_css, render_sidebar, render_page_header
from core.pdf_export import generate_quotation_pdf

st.set_page_config(page_title="Export PDF", page_icon="📄", layout="wide")
initialize_state()
inject_global_css()

render_sidebar(st.session_state.profile, st.session_state.results)
render_page_header("📄 Export PDF Quotation", "Generate a client-ready quotation PDF with system sizing and pricing.")

profile = st.session_state.profile
appliances = st.session_state.appliances
results = st.session_state.results

if not results:
    st.warning("Pehle Results page par ja kar system calculate karo.")
else:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    pdf_buffer = generate_quotation_pdf(profile, appliances, results)
    st.download_button(
        label="Download Quotation PDF",
        data=pdf_buffer,
        file_name="solar_quotation.pdf",
        mime="application/pdf"
    )
    st.markdown("</div>", unsafe_allow_html=True)
