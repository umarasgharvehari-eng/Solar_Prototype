import streamlit as st
from utils.session import initialize_state
from core.pdf_export import generate_quotation_pdf

initialize_state()

st.title("📄 Export PDF Quotation")

profile = st.session_state.get("profile", {})
appliances = st.session_state.get("appliances", [])
results = st.session_state.get("results", {})

if not results:
    st.warning("Pehle Results page par system calculate karo.")
else:
    pdf_buffer = generate_quotation_pdf(profile, appliances, results)

    st.download_button(
        label="Download Quotation PDF",
        data=pdf_buffer,
        file_name="solar_quotation.pdf",
        mime="application/pdf"
    )
