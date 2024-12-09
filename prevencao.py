import streamlit as st
from import_data import *
from funcoes_graficos import *

st.title("✅ Prevenção")

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
    st.text("Programas de prevenção e proteção para quais formas de violência contra a criança e o adolescente por Estado")
    st.plotly_chart(grafico_barra_horizontal(18, df_entidades_levantamentos), key="resposta_18", use_container_width=True)

with col2:
    st.text("Campanhas realizadas para conscientização da sociedade, com vistas acombater a violência institucional, promovendo a identificação das violações de direitos e garantias de crianças e adolescentes e a divulgação dos serviços de proteção e dos fluxos de atendimento por Estado")
    st.plotly_chart(grafico_barra_horizontal(19, df_entidades_levantamentos), key="resposta_19", use_container_width=True)


col3, col4 = st.columns([2,3], gap="large", vertical_alignment="top")

with col3:
    st.text("Estados nos quais os profissionais tem acesso à formação continuada e capacitação sobre prevenção, identificação de evidências, diagnóstico e enfrentamento de todas as formas de violência contra a criança e o adolescente")
    st.plotly_chart(grafico_pizza(20, df_entidades_levantamentos), key="resposta_20", use_container_width=True)

with col4:
    st.text("Profissionais que possuem acesso garantido e prioritário à formação continuada e capacitação por Estado")
    st.plotly_chart(grafico_barra_horizontal(21, df_entidades_levantamentos), key="resposta_21", use_container_width=True)


col5, col6 = st.columns([2,3], gap="large", vertical_alignment="top")

with col5:
    st.text("Estados nos quais os profissionais possuem especialização e atualização, em programas que contemplem a especificidade da primeira infância e a estratégia da intersetorialidade na promoção do desenvolvimento integral")
    st.plotly_chart(grafico_pizza(23, df_entidades_levantamentos), key="resposta_23", use_container_width=True)

with col6:
    st.text("Profissionais possuem especialização e atualização, em programas que contemplam a especificidade da primeira infância por Estado")
    st.plotly_chart(grafico_barra_horizontal(85, df_entidades_levantamentos), key="resposta_85", use_container_width=True)


col7, col8 = st.columns(2, gap="large", vertical_alignment="top")

with col7:
    st.text("Estados nos quais o poder público estadual estabeleceu matriz intersetorial de capacitação para os profissionais do sistema de garantia de direitos da criança e do adolescente vítima ou testemunha de violência")
    st.plotly_chart(grafico_pizza(86, df_entidades_levantamentos), key="resposta_86", use_container_width=True)

with col8:
    st.text("Estados que possuem açoes de promoção da parentalidade positiva e do direito ao brincar, em programas ja existentes ou novos, no ambito das respectivas competências")
    st.plotly_chart(grafico_pizza(89, df_entidades_levantamentos, .4), key="resposta_89", use_container_width=True)


col9, col10 = st.columns(2, gap="large", vertical_alignment="top")

with col9:
    st.text("Estados nos quais existe atuação articulada entre os entes federativos na execução de ações destinadas a coibir o uso de castigo físico ou de tratamento cruel ou degradante e difundir formas não violentas de educação de crianças e de adolescentes")
    st.plotly_chart(grafico_pizza(24, df_entidades_levantamentos, .4), key="resposta_24", use_container_width=True)

with col10:
    st.text("Estados nos quais conteúdos relativos aos direitos humanos e à prevenção de todas as formas de violência contra a criança e o adolescente estão incluídos nos curriculos da educação infantil, fundamental e médio")
    st.plotly_chart(grafico_pizza(26, df_entidades_levantamentos), key="resposta_26", use_container_width=True)


st.text("Estados que colaboraram com os municípios para a elaboração de um protocolo que estabeleça medidas de proteçãoà criança e ao adolescente contra qualquer forma de violência no âmbito escolar")
st.plotly_chart(grafico_mapa_brasil(87, df_entidades_levantamentos), key="resposta_87", use_container_width=True)

st.text("Nos casos em que o profissional da educação identifica ou a criança/adolescente revela a ele atos de violência, inclusive no ambiente escolar, são adotadas as seguintes medidas por Estado:")
st.plotly_chart(grafico_barra_horizontal(30, df_entidades_levantamentos), key="resposta_30", use_container_width=True)