import streamlit as st
from import_data import *
from funcoes_graficos import *

st.title("⚖️ Repressão e Acolhimento")

uf_selecao = st.sidebar.selectbox(
    "Estado", 
    estados["uf"],
    index=None,
    placeholder="Selecione um Estado...",
)

if uf_selecao:
    df_entidades_levantamentos = df_entidades_levantamentos[(df_entidades_levantamentos["uf"]==uf_selecao)]

print(df_entidades_levantamentos.columns)
col1, col2 = st.columns([2,3], vertical_alignment="top")

with col1:
    st.text("Estados nos quais existe procedimento para identificar casos de violência sexual em ambiente escolar da rede estadual")
    st.plotly_chart(grafico_pizza(29, df_entidades_levantamentos), key="resposta_29", use_container_width=True)

with col2:
    st.text("Estados que existe protocolo definido estabelecendo a máxima prioridade ao atendimento das crianças na faixa etária da primeira infância com suspeita ou confirmação de violência de qualquer natureza, nas seguintes instituições:")
    st.plotly_chart(grafico_barra_horizontal(32, df_entidades_levantamentos), key="resposta_32", use_container_width=True)


col3, col4 = st.columns([3,2], vertical_alignment="top")

with col3:
    st.text("Instituições em que é garantida a urgência e a celeridade necessárias ao atendimento de saúde e à produção probatória, preservada a confidencialidade, nos casos de violência sexual contra crianças e adolescentes de qualquer idade, nas seguintes instituições, por Estado:")
    st.plotly_chart(grafico_barra_horizontal(33, df_entidades_levantamentos), key="resposta_33", use_container_width=True)

with col4:
    st.text("Estados nos quais existe, no âmbito do Sistema Unico de Saúde (SUS), serviços para atenção integral à criança e ao adolescente em situação de violência, de forma a garantir o atendimento acolhedor")
    st.plotly_chart(grafico_pizza(34, df_entidades_levantamentos), key="resposta_34", use_container_width=True)

st.text("Atendimentos realizados em casos de violência sexual por profissionais, por Estado:")
st.plotly_chart(grafico_barra_horizontal(35, df_entidades_levantamentos), key="resposta_35", use_container_width=True)


col5, col6, col7, col8 = st.columns(4, vertical_alignment="top")

with col5:
    st.text("Estados que fornecem assistência psicossocial especializada às crianças e adolescentes vítimas de violênciae testemunhas")
    st.plotly_chart(grafico_pizza(37, df_entidades_levantamentos), key="resposta_37", use_container_width=True)

with col6:
    st.text("Estados que possuem equipes multidisciplinares destinadas a assessorar as DPCAs")
    st.plotly_chart(grafico_pizza(40, df_entidades_levantamentos, .4), key="resposta_40", use_container_width=True)

with col7:
    st.text("Estados que, caso não exista delegacia especializada, a vítima é encaminhada prioritariamente para a delegacia especializada em temas de direitos humanos")
    st.plotly_chart(grafico_pizza(42, df_entidades_levantamentos), key="resposta_42", use_container_width=True)

with col8:
    st.text("Estados que existe Centro de Referência Especializado de Assistência Social - CREAS em todos os municipios acima de 20.000 habitantes")
    st.plotly_chart(grafico_pizza(46, df_entidades_levantamentos, .4), key="resposta_46", use_container_width=True)


col9, col10, col11, col12 = st.columns(4, vertical_alignment="top")

with col5:
    st.text("Estados com pelo menos 1 advogado em todos os CREAS")
    st.plotly_chart(grafico_pizza(47, df_entidades_levantamentos), key="resposta_47", use_container_width=True)

with col6:
    st.text("Estados onde existe a oferta dos serviços de Y acolhimento para as crianças e os adolescentes")
    st.plotly_chart(grafico_pizza(49, df_entidades_levantamentos, .4), key="resposta_49", use_container_width=True)

with col7:
    st.text("A Secretaria de Assistência Social realiza o monitoramento e a avaliação da atividade de elaboração dos planos individuais e familiares de atendimento de crianças em serviço de acolhimento, valorizando a participação da criança e do adolescente e, sempre que possível, a preservação dos vínculos familiares no âmbito do Sistema Unico de Assistência Social (SUAS)")
    st.plotly_chart(grafico_pizza(48, df_entidades_levantamentos), key="resposta_48", use_container_width=True)

with col8:
    st.text("Estados que existem Varas da Infância e da Juventude específicas, em todas as comarcas que correspondam a municípios acima de 50.000 de habitantes")
    st.plotly_chart(grafico_pizza(52, df_entidades_levantamentos, .4), key="resposta_52", use_container_width=True)


st.text("Estados que estabeleceram dotações orçamentárias específicas, nos exercícios financeiros de 2023 e 2024, para manutenção dos serviços de acolhimento mantido pelo Estado")
st.plotly_chart(grafico_mapa_brasil(51, df_entidades_levantamentos), key="resposta_51", use_container_width=True)


col13, col14 = st.columns(2, vertical_alignment="top")

with col13:
    st.text("Caso não existam varas especializadas em crimes contra a criança e o adolescente, o julgamento e a execução das causas decorrente das práticas de violência ficam a cargo dos juizados ou varas especializadas em violência doméstica e temas afins?")
    st.plotly_chart(grafico_pizza(91, df_entidades_levantamentos), key="resposta_91", use_container_width=True)

with col14:
    st.text("Estados onde os serviços de acolhimento possuem capacidade e infrastrutura necessária para atendimento da demanda de todo o território")
    st.plotly_chart(grafico_pizza(50, df_entidades_levantamentos, .4), key="resposta_50", use_container_width=True)

st.text("Critérios atendidos por Estado na realização do depoimento especial no âmbito do Poder Judiciário:")
st.plotly_chart(grafico_barra_horizontal(55, df_entidades_levantamentos), key="resposta_55", use_container_width=True)


col15, col16 = st.columns([3,2], vertical_alignment="top")

with col15:
    st.text("Panorama da realização da escuta especializada na capital do Estado, por meio de procedimentos de atendimento condizentes com os princípios estabelecidos no art. 2° do Decreto 9.603/2018 e as regras dos arts. 19 e 20 do mesmo normativo, e indicação dos órgãos da rede de proteção?")
    st.plotly_chart(grafico_barra_horizontal(56, df_entidades_levantamentos), key="resposta_56", use_container_width=True)

with col16:
    st.text("Estados onde existem ações articuladas e coordenadas sobre o acolhimento e o atendimento integral das crianças e dos adolescentes vítimas ou testemunhas de violência que envolvam os sistemas de justiça, segurança pública, assistência social, educação e saúde")
    st.plotly_chart(grafico_pizza(59, df_entidades_levantamentos, .4), key="resposta_59", use_container_width=True)

st.text("Estados que criaram centros integrados compostos por atores dos órgãos, os programas, os serviços e equipamentos das políticas setoriais que compõem o sistema de garantia de direitos, para atendimento de casos de suspeita ou de confirmação de violência contra crianças e adolescentes")
st.plotly_chart(grafico_mapa_brasil(57, df_entidades_levantamentos), key="resposta_57", use_container_width=True)


col17, col18 = st.columns(2, vertical_alignment="top")

with col17:
    st.text("Atendimentos que compõe os centros integrados existentes:")
    st.plotly_chart(grafico_barra_horizontal(58, df_entidades_levantamentos), key="resposta_58", use_container_width=True)

with col18:
    st.text("Dados existentes no modelo de registro de informações para o compartilhamento do SGDCA, no âmbitos dos Centros Integrados existentes:")
    st.plotly_chart(grafico_barra_horizontal(90, df_entidades_levantamentos), key="resposta_90", use_container_width=True)


col19, col20 = st.columns([2,3], vertical_alignment="top")

with col19:
    st.text("Estados onde existe procedimento operacional padrão - POP, na polícia civil, com regras sobre o atendimento e o registro da ocorrência policial em crimes relacionados à violência contra crianças e adolescentes")
    st.plotly_chart(grafico_pizza(43, df_entidades_levantamentos, .4), key="resposta_43", use_container_width=True)

with col20:
    st.text("Os Procedimentos Operacional Padrão - POPs observam as seguintes regras:")
    st.plotly_chart(grafico_barra_horizontal(44, df_entidades_levantamentos), key="resposta_44", use_container_width=True)

st.text("Critérios que são atendidos nos Estados onde o depoimento especial é realizado na Polícia Civil:")
st.plotly_chart(grafico_barra_horizontal(45, df_entidades_levantamentos), key="resposta_45", use_container_width=True)


col21, col22, col23 = st.columns(3, vertical_alignment="top")

with col21:
    st.text("Estados onde é aplicado fluxo de atendimento diferenciado para crianças e adolescentes pertencentes a povos e comunidades tradicionais")
    st.plotly_chart(grafico_pizza(61, df_entidades_levantamentos), key="resposta_61", use_container_width=True)
with col22:
    st.text("Em caso positivo, existe uma articulação dos serviços socioassistenciais com a Coordenação Regional da Fundação Nacional do Índio-FUNAI e com o Distrito Sanitário Especial Indígena-DSEl do Ministério da Saúde, por Estado:")
    st.plotly_chart(grafico_pizza(62, df_entidades_levantamentos, .4), key="resposta_62", use_container_width=True)
with col23:
    st.text("Estados onde existe programa de proteção e compensação das vítimas, testemunhas e noticiantes ou denunciantes de ação ou omissão, que constitua violência domestica e familiar contra a criança e o adolescente")
    st.plotly_chart(grafico_pizza(64, df_entidades_levantamentos), key="resposta_64", use_container_width=True)


col24, col25, col26 = st.columns(3, vertical_alignment="top")

with col24:
    st.text("Estados onde existe procedimento operacional padrão - POP, no âmbito da polícia militar com regras sobre o atendimento de ocorrências com crianças e/ou adolescentes (situações em que são autores, vítimas ou testemunhas)")
    st.plotly_chart(grafico_pizza(70, df_entidades_levantamentos), key="resposta_70", use_container_width=True)
with col25:
    st.text("Estados onde existe unidades especializadas no âmbito da Defensoria Pública, nos termos do art. 23 da Lei n° 13.431/17, sobre a violação dos direitos de crianças e adolescentes")
    st.plotly_chart(grafico_pizza(68, df_entidades_levantamentos, .4), key="resposta_68", use_container_width=True)
with col26:
    st.text("Estados com ações civis públicas em trâmite sobre casos de inexistência ou de insuficiência de atuação dos órgãos estaduais e/ou municipais, havendo inviabilidade de articulação com a rede protetiva? (Excluir ações já arquivadas)")
    st.plotly_chart(grafico_pizza(69, df_entidades_levantamentos), key="resposta_69", use_container_width=True)


st.text("Estados onde existem Promotorias da Infância e Juventude especializadas em todas as comarcas da Capital e nas cidades acima de 100.000 habitantes")
st.plotly_chart(grafico_mapa_brasil(65, df_entidades_levantamentos), key="resposta_65", use_container_width=True)