import pandas as pd
import plotly.express as px
from import_data import *

# Configurando as cores
amarelo =  "#EDC40C" # "#E1C233"
laranja = "#E66C37"
cinza = "#ccc"
verde = "#58BDB6"
azul = "#1C6F9D"
sim = azul
nao = verde

# Configurando tamanho dos gráficos de pizza
width_pizza = 275
height_pizza = 275

######################################
# Função que cria gráfico de mapa do Brasil com respostas SIM e NÃO
######################################
def grafico_mapa_brasil(pergunta_id, df_entidades_levantamentos):
    filtro_pergunta = df_respostas[(df_respostas["pergunta_id"]==pergunta_id)][['resposta_levantamento_id','boolean_answer']]

    df_resposta = pd.merge(
        df_entidades_levantamentos, filtro_pergunta, left_on="id_x", right_on="resposta_levantamento_id", how="left"
        )[['uf', 'boolean_answer']]

    df_resposta["boolean_answer"] = df_resposta["boolean_answer"].replace({
        True: "Sim",
        False: "Não",
        None: "Não Respondeu"  # Alternativa para valores nulos (None ou NaN)
    })

    # Gerar o mapa com Plotly Express
    fig_mapa = px.choropleth(
        df_resposta,
        geojson=geojson_url,
        locations="uf",
        featureidkey="properties.sigla",  # Códigos ISO no GeoJSON
        color="boolean_answer",
        color_discrete_map={"Sim": sim, "Não": nao, "Não Respondeu": cinza} ,
        labels={"boolean_answer": "Resposta"},
        hover_name="uf",
    )

    fig_mapa.update_geos(
        fitbounds="locations",
        visible=False
    )

    fig_mapa.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",  # Fundo do gráfico
        geo=dict(bgcolor="rgba(0,0,0,0)")  # Fundo do mapa
    )

    return fig_mapa


######################################
# Função que cria gráfico de pizza com respostas SIM e NÃO
######################################
def grafico_pizza(pergunta_id, df_entidades_levantamentos, hole=None):
    filtro_pergunta = df_respostas[(df_respostas["pergunta_id"]==pergunta_id)][['resposta_levantamento_id','boolean_answer']]

    df_resposta = pd.merge(
        df_entidades_levantamentos, filtro_pergunta, left_on="id_x", right_on="resposta_levantamento_id", how="inner"
    )

    pie_data = pd.DataFrame({
        'Resposta': ['Sim', 'Não'],
        'Quantidade': [df_resposta[(df_resposta['boolean_answer']==True)]['boolean_answer'].count(), df_resposta[(df_resposta['boolean_answer']==False)]['boolean_answer'].count()]
    })

    fig_resposta = px.pie(
        pie_data, 
        values='Quantidade', 
        names='Resposta',
        color='Resposta',
        #title="Plano Estadual possui alinhamento com o Plano Nacional de Enfrentamento da Violência contra Crianças e Adolescentes?",
        color_discrete_map={'Sim': sim, 'Não': nao},
        hole=hole
    )
    fig_resposta.update_traces(textposition='inside', textinfo='percent+value')
    fig_resposta.update_layout(
        width=width_pizza,  # Largura em pixels
        height=height_pizza  # Altura em pixels
    )

    return fig_resposta


######################################
# Função que cria gráfico de barra horizontal
######################################
def grafico_barra_horizontal(pergunta_id, df_entidades_levantamentos):
    filtro_pergunta = df_respostas[(df_respostas["pergunta_id"]==pergunta_id)]

    df_resposta = pd.merge(
        df_entidades_levantamentos, filtro_pergunta, left_on="id_x", right_on="resposta_levantamento_id", how="inner"
    )[['id']]

    df_resposta = pd.merge(
        df_resposta, df_resposta_opcoes, left_on="id", right_on="respostapergunta_id", how="inner"
    )

    df_resposta = pd.merge(
        df_resposta, df_opcoes, left_on="opcao_id", right_on="id", how="inner"
    )

    count_df_resposta = df_resposta['texto'].value_counts().reset_index()
    count_df_resposta.columns = ['texto', 'total']

    # Ordenar os dados pelo total
    count_df_resposta = count_df_resposta.sort_values('total', ascending=True)

    # Criar gráfico de barras horizontais com Plotly
    fig_resposta = px.bar(
        count_df_resposta,
        x='total',
        y='texto',
        orientation='h',
        text='total',
        #title='Nos planos estaduais existentes foram estabelecidos',
        color_discrete_sequence=[nao, sim],
        range_x=[0, 20],
    )

    fig_resposta.update_layout(
        xaxis_title='',  # Sem título para o eixo X
        yaxis_title='',  # Sem título para o eixo Y
        showlegend=False,

    )

    fig_resposta.update_traces(
        textfont_size=14, 
        textangle=0, 
        cliponaxis=False
        )


    return fig_resposta