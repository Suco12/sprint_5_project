import streamlit as st
import pandas as pd 
import plotly.express as px  # Correção aqui!

st.header('Análise de veículos nos EUA')

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Gerar gráfico de distribuição de marcas de veículos')

if hist_button:
    st.write('Criando histograma para a coluna odometer')
    fig = px.histogram(car_data, x='odometer', nbins=50, title='Distribuição de odômetro dos veículos')
    st.plotly_chart(fig)