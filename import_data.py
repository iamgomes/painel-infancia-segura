import streamlit as st
import pandas as pd

# Lista de estados
estados = pd.DataFrame({
    "uf": ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"],
})

# Recebe um csv e converte em dataframe usando o cache
#@st.cache_data
def convert_csv(file):
    return pd.read_csv(file, sep=";")


#Clear all in-memory and on-disk data caches.
st.cache_data.clear()

# Importando os dados
df_capitais = convert_csv('dados/capitais.csv')
df_entidades = convert_csv('dados/entidades.csv')
df_levantamentos = convert_csv('dados/levantamentos.csv')
df_respostas = convert_csv('dados/respostas.csv')
df_perguntas = convert_csv('dados/perguntas.csv')
df_opcoes = convert_csv('dados/opcoes.csv')
df_resposta_opcoes = convert_csv('dados/resposta_opcoes.csv')
df_conselhos = pd.read_csv('dados/quantidade_conselho_tutelar.csv', sep=";")
df_fmdca = pd.read_csv('dados/dados_fmdca.csv', sep=";")

# Filtrando tribunais
df_entidades = df_entidades[(df_entidades["esfera"]!="M")]
# Remover a parte inicial (padrão: letra maiúscula seguida de ')')
df_opcoes['texto'] = df_opcoes['texto'].str.replace(r'^[A-Z]\)\s*', '', regex=True)
# GeoJSON do Brasil
geojson_url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"

# Realizar os joins
df_capitais_entidades = pd.merge(
    df_entidades, df_capitais, left_on="municipio_id", right_on="ibge", how="inner"
)[['id', 'nome_x', 'uf']]

df_entidades_levantamentos = pd.merge(
    df_levantamentos, df_capitais_entidades, left_on="entidade_id", right_on="id", how="right"
)[['id_x', 'entidade_id', 'nome_x', 'uf']]