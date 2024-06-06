import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

st.image('https://images.squarespace-cdn.com/content/v1/51cdafc4e4b09eb676a64e68/1470951917131-VO6KK2XIFP4LPLCYW7YU/McQueen15.jpg')
st.header('Lightning McQueen Vendas', divider='rainbow')
st.caption(':red_car: Dados sobre vendas da concessionária Lightning McQueen')
car_data
hist_button = st.button('Criar Histograma') # criar um botão

if hist_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

# criar um histograma
    fig = px.histogram(car_data, x="odometer")

# exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

print()
# criar um graf dispersão
disp_button = st.button('Criar Gráfico de Dispersão') # criar um botão

if disp_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

# criar um grafico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
    st.plotly_chart(fig, use_container_width=True)


