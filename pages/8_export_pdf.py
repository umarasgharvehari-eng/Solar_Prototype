import streamlit as st
import pandas as pd
from core.pdf_export import build_pdf
from utils.ui import top_hero
st.title("📄 Export PDF Quotation")

st.markdown("""
<div style="
background: white;
padding: 20px;
border-radius: 20px;
box-shadow: 0 8px 24px rgba(15,23,42,0.08);
border: 1px solid #e2e8f0;
margin-bottom: 18px;">
Generate a clean client-ready quotation PDF for your solar proposal.
</div>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Export PDF", layout="wide")
top_hero("Export Quotation", "Professional PDF quotation aur CSV appliances export download karein.")

results = st.session_state.results
if not results:
    st.warning("Pehle Results page par calculation complete karein.")
else:
    pdf_buffer = build_pdf(
        st.session_state.profile,
        st.session_state.results,
        st.session_state.appliances,
        st.session_state.roof,
        st.session_state.pricing,
    )
    filename = f"solar_quote_{(st.session_state.profile.get('name') or 'customer').replace(' ', '_')}.pdf"
    st.download_button(
        "Download PDF Quotation",
        data=pdf_buffer,
        file_name=filename,
        mime="application/pdf",
        use_container_width=True,
    )

    appliance_df = pd.DataFrame(st.session_state.appliances)
    csv_bytes = appliance_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download Appliances CSV",
        data=csv_bytes,
        file_name="appliances.csv",
        mime="text/csv",
        use_container_width=True,
    )
