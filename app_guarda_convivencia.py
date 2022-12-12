import streamlit as st
from datetime import datetime, timedelta

# Adicionar um título na página
st.title('APP Guarda e Convivência')

# Adicionar uma barra lateral
st.sidebar.title('Sobre o APP')
st.sidebar.markdown('Este é um app que calcula quinzenas e metades de férias.')
st.sidebar.write('Muitas vezes, os pais divorciados enfrentam dificuldades para organizar os períodos de guarda'
                 ' e convivência ao longo do ano de modo antecipado. '
                 'Esta aplicação visa facilitar a organização dos períodos de guarda e convivência, '
                 'permitindo que os pais visualisem a lista completa dos períodos alternados de 15 dias durante o ano corrente. '
                 'Além disso, ela faz o cálculo dos períodos de férias.'
                 )

# Criar um calendário para a seleção da data
st.subheader('Cálculo da convivência quinzenal:')
data_date = st.date_input('Selecione a data:',
                          key='data_date')

# Converter a data em um objeto datetime
data_str = data_date.strftime('%Y-%m-%d')
data = datetime.strptime(data_str, '%Y-%m-%d')


# Criar uma lista para armazenar as datas resultantes
datas = []

# Enquanto a data não for do próximo ano, adicionar 15 dias
while True:
    # Adicionar 15 dias a data
    data += timedelta(days=15)

    # Verificar se a data já é do próximo ano
    if data.year != datetime.now().year:
        break

    # Adicionar a data à lista
    datas.append(data)

# Exibir um texto explicativo
st.markdown(
    'Abaixo estão todas as datas do ano que sucedem a data escolhida, de 15 em 15 dias:'
)

# Exibir as datas resultantes em uma lista
lista_datas = ([data.strftime('%d/%m/%Y') for data in datas])
st.write(lista_datas)


# Adiciona a seção metade das férias 
st.subheader('Cálculo das férias:')

# Cria dois calendários para seleção das datas de início e de término das férias
data_inicio = st.date_input('Selecione a data de início das férias:', key='data_inicio')
data_fim = st.date_input('Selecione a data de término das férias:', key='data_fim')

# Converte as datas em objetos datetime
data_inicio_str = data_inicio.strftime('%Y-%m-%d')
data_fim_str = data_fim.strftime('%Y-%m-%d')
data_inicio = datetime.strptime(data_inicio_str, '%Y-%m-%d')
data_fim = datetime.strptime(data_fim_str, '%Y-%m-%d')

# Calcula o número de dias das férias
num_dias = (data_fim - data_inicio).days

# Calcula a metade das férias
metade_ferias = num_dias // 2

# Exibe as datas de início e de término das férias
st.write(f'Início das férias: {data_inicio.strftime("%d/%m/%Y")}')
st.write(f'Término das férias: {data_fim.strftime("%d/%m/%Y")}')

# Exibe a data de término da primeira metade e de início da segunda metade
data_fim_primeira_metade = data_inicio + timedelta(days=metade_ferias)
data_inicio_segunda_metade = data_fim_primeira_metade + timedelta(days=1)

st.write(f'Fim da primeira metade das férias: {data_fim_primeira_metade.strftime("%d/%m/%Y")}')
st.write(f'Início da segunda metade das férias: {data_inicio_segunda_metade.strftime("%d/%m/%Y")}')

# Obtém o ano corrente
ano_atual = datetime.now().year

# Calcula o número de dias das férias
num_dias = (data_fim - data_inicio).days

# Calcular a metade das férias
metade_ferias = num_dias // 2
