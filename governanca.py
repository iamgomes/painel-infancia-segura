import streamlit as st
from import_data import *
from funcoes_graficos import *

# Título da Página
st.title("📋 Governança")

uf_selecao = st.sidebar.selectbox(
    "Estado", 
    estados["uf"],
    index=None,
    placeholder="Selecione um Estado...",
)

if uf_selecao:
    df_entidades_levantamentos = df_entidades_levantamentos[(df_entidades_levantamentos["uf"]==uf_selecao)]

######################################
# Gráficos da faixa 1
######################################
st.markdown("##### Estados que possuem Plano Estadual para o enfrentamento à violência contra crianças e adolescentes ou instrumento similar")
st.plotly_chart(grafico_mapa_brasil(1, df_entidades_levantamentos), key="resposta_1", use_container_width=True)

col1, col2 = st.columns(2, vertical_alignment="top")

with col1:
        st.text("Estados que possuem Plano Estadual ancorado em algum instrumento normativo")
        st.plotly_chart(grafico_pizza(2, df_entidades_levantamentos), key="resposta_2", use_container_width=True)

        st.text("Estados com plano publicado em veículo oficial e disponível para sociedade")
        st.plotly_chart(grafico_pizza(4, df_entidades_levantamentos, .4), key="resposta_4", use_container_width=True)

with col2:
        st.text("Estados com Plano Estadual alinhado com o Plano Nacional de enfrentamento da violência contra crianças e adolescentes")
        st.plotly_chart(grafico_pizza(3, df_entidades_levantamentos, .4), key="resposta_3", use_container_width=True)

        st.text("Estados nos quais houve a instituição de ciclos periódicos de avaliação e monitoramento do plano estadual")
        st.plotly_chart(grafico_pizza(7, df_entidades_levantamentos), key="resposta_7", use_container_width=True)

col3, col4 = st.columns(2, vertical_alignment="top")

with col3:
    st.text("Ações realizadas no processo de construção dos planos nos Estados que possuem Plano Estadual")
    st.plotly_chart(grafico_barra_horizontal(5, df_entidades_levantamentos), key="resposta_5", use_container_width=True)

with col4:
    st.text("Nos planos estaduais existentes foram estabelecidos:")
    st.plotly_chart(grafico_barra_horizontal(6, df_entidades_levantamentos), key="resposta_6", use_container_width=True)


######################################
# Gráficos da faixa 2
######################################
st.markdown("##### Estados que estabeleceram normas sobre o sistema de garantia de direitos da criança e do adolescente vítima ou testemunha de violência")
st.plotly_chart(grafico_mapa_brasil(13, df_entidades_levantamentos), key="resposta_13", use_container_width=True)

col5, col6, col7 = st.columns(3, vertical_alignment="top")

with col5:
    st.text("Estados que possuem Comitê Intersetorial de políticas públicas para a primeira infância?")
    st.plotly_chart(grafico_pizza(8, df_entidades_levantamentos), key="resposta_8", use_container_width=True)

    st.text("Estados que receberam do MJSP orientação sobre programa ou ação na temática da violência contra a criança e o adolescente ou da implementação da lei da escuta especializada")
    st.plotly_chart(grafico_pizza(22, df_entidades_levantamentos), key="resposta_22", use_container_width=True)

with col6:
    st.text("Estados nos quais o Comitê Intersetorial de políticas públicas para a primeira infância está em efetivo funcionamento")
    st.plotly_chart(grafico_pizza(9, df_entidades_levantamentos, 0.4), key="resposta_9", use_container_width=True)

    st.text("Estados nos instituiram Comitê de gestão colegiada da rede de cuidado e de proteção social das crianças e dos adolescentes vítimas ou testemunhas de violência")
    st.plotly_chart(grafico_pizza(14,df_entidades_levantamentos, 0.4), key="resposta_14", use_container_width=True)

with col7:
    st.text("Estados nos quais existe uma articulação permanente entre os órgãos responsáveis pela coordenação do comitê intersetorial no âmbito federal e estadual")
    st.plotly_chart(grafico_pizza(10, df_entidades_levantamentos), key="resposta_10", use_container_width=True)

    st.text("Estados nos quais o Comitê de gestão colegiada da rede de cuidado está em efetivo funcionamento")
    st.plotly_chart(grafico_pizza(15, df_entidades_levantamentos), key="resposta_15", use_container_width=True)


######################################
# Gráficos da faixa 3
######################################
st.markdown("##### Estados que estabeleceram dotações orçamentárias específicas, em de 2024, para a implementação de ações específicas do sistema de garantias de direitos da criança e do adolescente vítima ou testemunha de violência?")
st.plotly_chart(grafico_mapa_brasil(17, df_entidades_levantamentos), key="resposta_17", use_container_width=True)

col8, col9 = st.columns(2, vertical_alignment="top")

with col8:
    st.text("Estados nos quais a União ofereceu técnica na elaboração de planos estaduais para a primeira infância que articulem os diferentes setores, com vistas a uma abordagem multi e intersetorial")
    st.plotly_chart(grafico_pizza(11, df_entidades_levantamentos), key="resposta_11", use_container_width=True)
with col9:
    st.text("Estados que estabeleceram as diretrizes para que os municípios definam o fluxo de atendimento das crianças e adolescentes vítimas ou testemunhas de violência, conforme art. 9°, Il do Decreto 9.603/2018")
    st.plotly_chart(grafico_pizza(16, df_entidades_levantamentos, .4), key="resposta_16", use_container_width=True)