import streamlit as st
from import_data import *
from graficos import *

st.title("👨‍👩‍👧‍👦 Distribuição espacial e proporcional de Conselhos Tutelares (CT) no Brasil - 2024")

def formatar_numero(numero):
    if numero >= 1_000_000:  # Para milhões
        valor_formatado = round(numero / 1_000_000, 1)  # Arredonda para 1 casa decimal
        return f"{valor_formatado} Milhões"
    elif numero >= 1_000:  # Para milhares
        valor_formatado = round(numero / 1_000, 1)  # Arredonda para 1 casa decimal
        return f"{valor_formatado} Mil"
    else:  # Para valores menores que mil
        return str(numero)
    
def conselhos_por_100k(conselhos, populacao):
    # Calcula a quantidade de conselhos por 100 mil habitantes
    return (conselhos / populacao) * 100000

tabela = df_conselhos.groupby(['ESTADO','UF'])[['Pop_Resd_Total_2024_PNAD','QTD_CONSELHO_TUTELAR']].sum()

# Criando uma nova coluna aplicando a função conselhos_por_100k
tabela['Conselhos por 100k'] = tabela.apply(
    lambda row: round(conselhos_por_100k(row['QTD_CONSELHO_TUTELAR'], row['Pop_Resd_Total_2024_PNAD'])),
    axis=1
)

# Resetando o índice e acessando como coluna
tabela.reset_index(inplace=True)
#tabela.set_index('UF')

# Alterando os nomes das colunas
tabela = tabela.rename(columns={
    'ESTADO': 'Estado',
    'Pop_Resd_Total_2024_PNAD': 'População Residente Total - PNAD 2024',
    'QTD_CONSELHO_TUTELAR': 'Total de Conselhos Tutelares'
})

tabela = tabela[['UF', 'Estado', 'População Residente Total - PNAD 2024', 'Total de Conselhos Tutelares', 'Conselhos por 100k']]

st.sidebar.header("Filtros")
uf_selecao = st.sidebar.selectbox(
    "Estado", 
    estados["uf"],
    index=None,
    placeholder="Selecione um Estado...",
)

if uf_selecao:
    tabela = tabela[(tabela["UF"]==uf_selecao)]

# Gerar o mapa com Plotly Express
fig_mapa = px.choropleth(
    tabela,
    geojson=geojson_url,
    locations="UF",
    featureidkey="properties.sigla",  # Códigos ISO no GeoJSON
    color="Conselhos por 100k",
    color_continuous_scale=[(0, cinza), (0.5, sim), (1, nao)], 
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
    total_conselhos = tabela["Total de Conselhos Tutelares"].sum()
    st.metric("Total de Conselhos Tutelares", total_conselhos)

with col2:
    total_pop = tabela["População Residente Total - PNAD 2024"].sum()
    st.metric("População Residente Total - PNAD 2024", formatar_numero(total_pop),)

with col3:
    st.metric("Conselhos Tutelares por 100 mil habitantes", round(conselhos_por_100k(total_conselhos, total_pop)))

st.plotly_chart(fig_mapa, key="mapa_conselho", use_container_width=True)

st.dataframe(
    tabela.sort_values(by='Conselhos por 100k', ascending=False),
        column_config={
        "População Residente Total - PNAD 2024": st.column_config.NumberColumn(
            format="%d",
        )
    },
    hide_index=True,
    use_container_width=True
)