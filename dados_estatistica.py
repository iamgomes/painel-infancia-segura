import streamlit as st
from import_data import *
from graficos import *

st.title("📈 Dados e Estatística")

st.sidebar.header("Filtros")
uf_selecao = st.sidebar.selectbox(
    "Estado", 
    estados["uf"],
    index=None,
    placeholder="Selecione um Estado...",
)

if uf_selecao:
    df_entidades_levantamentos = df_entidades_levantamentos[(df_entidades_levantamentos["uf"]==uf_selecao)]

col1, col2 = st.columns(2, gap="large", vertical_alignment="top")

with col1:
    titulo_71 = "Estados onde existem servicos de ouvidoria ou de resposta para recebimento de denuncias de violência integrado à rede de proteção"
    st.plotly_chart(grafico_pizza(71, df_entidades_levantamentos, titulo_71), key="resposta_71", use_container_width=True)

with col2:
    titulo_74 = "Estados onde os órgãos que integram o SGDCA estabeleceram parcerias com a finalidade de integrar todas as portas de entrada sobre a comunicação de violência contra crianças e adolescentes"
    st.plotly_chart(grafico_pizza(74, df_entidades_levantamentos, titulo_74, .4), key="resposta_74", use_container_width=True)

titulo_75 = "Entes do SGDCA que possuem sistema eletrônico próprio para registro e acompanhamento das demandas que envolvem crianças e adolescentes vítimas ou testemunhas de violência, por Estado:"
st.plotly_chart(grafico_barra_horizontal(75, df_entidades_levantamentos, titulo_75), key="resposta_75", use_container_width=True)


col3, col4 = st.columns(2, gap="large", vertical_alignment="top")

with col3:
    titulo_76 = "Existência de interoperabilidade entre os sistemas próprios utilizados pelos entes do SGDCA:"
    st.plotly_chart(grafico_pizza(76, df_entidades_levantamentos, titulo_76), key="resposta_76", use_container_width=True)

with col4:
    titulo_77 = "Existência de sistema eletrônico de informações que realiza a integração, de forma sigilosa, das informações produzidas pelo sistema de garantia"
    st.plotly_chart(grafico_pizza(77, df_entidades_levantamentos, titulo_77, .4), key="resposta_77", use_container_width=True)


col5, col6 = st.columns(2, gap="large", vertical_alignment="top")

with col5:
    titulo_80 = "Estados em que os órgãos do SGDCA realizam o mapeamento das ocorrências das formas de violência contra crianças e adolescentes"
    st.plotly_chart(grafico_pizza(80, df_entidades_levantamentos, titulo_80), key="resposta_80", use_container_width=True)

with col6:
    titulo_83 = "Qual o risco da criança e adolescente sofrer revitimização?"
    st.plotly_chart(grafico_pizza_com_legenda(83, df_entidades_levantamentos, titulo_83, .4), key="resposta_83", use_container_width=True)