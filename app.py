import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# Verificar si el archivo existe
st.write("Buscando archivo de datos...")
if os.path.exists('vehicles_us.csv'):
    st.success("Archivo vehicles_us.csv encontrado")
    car_data = pd.read_csv('vehicles_us.csv')
else:
    # Listar archivos disponibles para debug
    st.error("Archivo vehicles_us.csv NO encontrado")
    st.write("Archivos en el directorio:")
    for file in os.listdir('.'):
        st.write(f"- {file}")
    # Crear datos de ejemplo como fallback
    import numpy as np
    st.warning("Usando datos de ejemplo")
    car_data = pd.DataFrame({
        'odometer': np.random.randint(0, 200000, 1000),
        'price': np.random.randint(1000, 50000, 1000)
    })
