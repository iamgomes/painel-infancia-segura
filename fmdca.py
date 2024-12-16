import streamlit as st
from import_data import *
from graficos import *

st.title("🏛️ Distribuição espacial e proporcional dos Fundos Municipais de Direitos da Criança e do Adolescente (FMDCA) - 2024")

df_fmdca['Prop_Mun_FMCA_Tt_Mun'] = df_fmdca['Prop_Mun_FMCA_Tt_Mun'].replace(',', '')
df_fmdca["Proporção de Municípios com FMDCA (%)"] = df_fmdca["Prop_Mun_FMCA_Tt_Mun"] * 100

df_fmdca = df_fmdca[['UF', 'Estado', 'Qtd_mun_COM_FMCA', 'Qtd_Municipios', 'Proporção de Municípios com FMDCA (%)']]

# Alterando os nomes das colunas
df_fmdca = df_fmdca.rename(columns={
    'Qtd_mun_COM_FMCA': 'Total de FMDCA',
    'Qtd_Municipios': 'Total de Municípios',
})

st.sidebar.header("Filtros")
uf_selecao = st.sidebar.selectbox(
    "Estado", 
    estados["uf"],
    index=None,
    placeholder="Selecione um Estado...",
)

if uf_selecao:
    df_fmdca = df_fmdca[(df_fmdca["UF"]==uf_selecao)]

# Gerar o mapa com Plotly Express
fig_mapa = px.choropleth(
    df_fmdca,
    geojson=geojson_url,
    locations="UF",
    featureidkey="properties.sigla",  # Códigos ISO no GeoJSON
    color="Proporção de Municípios com FMDCA (%)",
    color_continuous_scale=[(0, cinza), (0.5, sim), (1, nao)],  # Degradê verde -> amarelo -> vermelho
)

fig_mapa.update_geos(
    fitbounds="locations",
    visible=False
)

fig_mapa.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",  # Fundo do gráfico
    geo=dict(bgcolor="rgba(0,0,0,0)")  # Fundo do mapa
)


col1, col2, col3 = st.columns(3, vertical_alignment="top")

with col1:
    total_mun = df_fmdca["Total de Municípios"].sum()
    st.metric("Total de Municípios", total_mun)

with col2:
    total_fmdca = df_fmdca["Total de FMDCA"].sum()
    st.metric("Total de FMDCA", total_fmdca)

with col3:
    media_fmdca = df_fmdca["Proporção de Municípios com FMDCA (%)"].mean()
    st.metric("Percentual de Municípios com FMDCA", f'{round(media_fmdca,1)}%')

st.plotly_chart(fig_mapa, key="mapa_fmdca", use_container_width=True)

st.dataframe(
    df_fmdca.sort_values(by='Proporção de Municípios com FMDCA (%)', ascending=False),
    column_config={
        "Proporção de Municípios com FMDCA (%)": st.column_config.NumberColumn(
            format="%.2f%%",
        )
    },
    hide_index=True,
    use_container_width=True
)