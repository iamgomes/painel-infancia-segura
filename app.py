import streamlit as st
import streamlit.components.v1 as components

# Configuração da página Streamlit
st.set_page_config(
    page_title="Infância Segura", 
    layout="wide",
    page_icon="assets/icon_logo_infancia_segura.svg",
)

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.logo(
    "assets/logo_infancia_segura.svg",
    icon_image="assets/icon_logo_infancia_segura.svg",
)

pages = {
    "Dimensões": [
        st.Page("visao_geral.py", title="Visão Geral", icon="🌐"),
        st.Page("governanca.py", title="Governança", icon="📋"),
        st.Page("prevencao.py", title="Prevenção", icon="✅"),
        st.Page("repressao.py", title="Repressão e Acolhimento", icon="⚖️"),
        st.Page("dados_estatistica.py", title="Dados e Estatística", icon="📈"),
        st.Page("conselho_tutelar.py", title="Conselho Tutelar", icon="👨‍👩‍👧‍👦"),
        st.Page("fmdca.py", title="FMDCA", icon="🏛️"),
    ],
}

pg = st.navigation(pages)
pg.run()