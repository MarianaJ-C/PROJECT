import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')  

st.title('Análisis de Vehículos Usados')

st.header('Exploración de Datos de Vehículos')

st.subheader('Primeras filas del dataset:')
st.write(df.head())  

show_histogram = st.checkbox('Mostrar Histograma de Precios')

show_scatter = st.checkbox('Mostrar Gráfico de Dispersión entre Precio y Millaje')

if show_histogram:
    fig_hist = px.histogram(df, x='price', nbins=30, title='Distribución de Precios de Vehículos')
    st.plotly_chart(fig_hist)

if show_scatter:
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Relación entre Precio y Millaje de Vehículos')
    st.plotly_chart(fig_scatter)
