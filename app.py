import streamlit as st
import pandas as pd

# Configuração da página Streamlit
st.set_page_config(
    page_title="Infância Segura", 
    layout="wide",
    page_icon="assets/icon_logo_infancia_segura.svg",
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.logo(
    "assets/logo_infancia_segura.svg",
    icon_image="assets/icon_logo_infancia_segura.svg",
    size="large"
)

pages = {
    "Dimensões": [
        st.Page("governanca.py", title="Governança", icon="📋"),
        st.Page("prevencao.py", title="Prevenção", icon="✅"),
        st.Page("repressao.py", title="Repressão e Acolhimento", icon="⚖️"),
        st.Page("dados_estatistica.py", title="Dados e Estatística", icon="📈"),
        st.Page("conselho_tutelar.py", title="Conselho Tutelar", icon="👨‍👩‍👧‍👦"),
        st.Page("fmdca.py", title="FMDCA", icon="🏛️"),
    ],
}

st.sidebar.header("Filtros")

pg = st.navigation(pages)
pg.run()