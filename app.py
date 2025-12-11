import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Configurar página
st.set_page_config(page_title="Dashboard de Coches", layout="wide")

# Título de la aplicación
st.title("Dashboard de Anuncios de Coches")
st.header("Análisis exploratorio de datos de vehículos")

# Leer datos
@st.cache_data
def load_data():
    try:
        data = pd.read_csv('vehicles_us.csv')
        return data
    except FileNotFoundError:
        st.error("Archivo vehicles_us.csv no encontrado")
        return pd.DataFrame()

car_data = load_data()

# Mostrar datos si existen
if not car_data.empty:
    st.write("### Vista previa de los datos")
    st.write(car_data.head())
    
    st.write(f"### Resumen del dataset")
    st.write(f"- **Total de registros:** {len(car_data)}")
    st.write(f"- **Total de columnas:** {len(car_data.columns)}")
    
    # Botón para histograma
    st.write("---")
    st.write("## Visualizaciones")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Histograma")
        if st.button('Mostrar histograma de odómetro'):
            fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
            fig.update_layout(
                title_text='Distribución del Odómetro',
                xaxis_title='Odómetro',
                yaxis_title='Frecuencia'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.write("### Gráfico de dispersión")
        if st.button('Mostrar dispersión Odómetro vs Precio'):
            fig = go.Figure(data=[go.Scatter(
                x=car_data['odometer'], 
                y=car_data['price'], 
                mode='markers',
                marker=dict(size=5, opacity=0.5)
            )])
            fig.update_layout(
                title_text='Relación entre Odómetro y Precio',
                xaxis_title='Odómetro',
                yaxis_title='Precio'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Casillas de verificación (opcional avanzado)
    st.write("---")
    st.write("### Opciones avanzadas")
    
    build_hist = st.checkbox('Mostrar histograma con casilla')
    build_scatter = st.checkbox('Mostrar gráfico de dispersión con casilla')
    
    if build_hist:
        st.write("Histograma del odómetro (usando casilla):")
        fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
        st.plotly_chart(fig, use_container_width=True)
    
    if build_scatter:
        st.write("Dispersión Odómetro vs Precio (usando casilla):")
        fig = go.Figure(data=[go.Scatter(
            x=car_data['odometer'], 
            y=car_data['price'], 
            mode='markers'
        )])
        st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Por favor, sube el archivo vehicles_us.csv a tu repositorio")
