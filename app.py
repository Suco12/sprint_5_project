import streamlit as st
import pandas as pd 
import plotly.express as px  # Correção aqui!

# Carregando os dados:
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho 
st.header('Análise de veículos nos EUA')

# Botão para histograma
hist_button = st.button('Gerar gráfico de distribuição de odômetro')
if hist_button:
    st.write('Criando histograma para a coluna odometer')
    fig = px.histogram(car_data, x='odometer', nbins=50, title='Distribuição de odômetro dos veículos')
    st.plotly_chart(fig, use_container_width=True)

# Botão para gráfico de dispersão
scatter_button = st.button('Gerar gráfico de dispersão')
if scatter_button:
    st.write('Criando gráfico de dispersão entre odômetro e preço')
    fig = px.scatter(car_data, x = 'odometer', y = 'price', title = 'Dispersão entre odômetro e preço dos veículos')
    st.plotly_chart(fig, use_container_width=True)