import streamlit as st
import pandas as pd
from core.pdf_export import build_pdf
from utils.ui import top_hero

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
