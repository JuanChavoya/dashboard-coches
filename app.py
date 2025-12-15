import streamlit as st
import pandas as pd
import os

st.title("Verificación de archivos")

# Listar todos los archivos en el directorio actual
st.write("### Archivos en el directorio actual:")
current_dir = os.listdir('.')
for file in current_dir:
    st.write(f"- {file}")

# Verificar si el CSV existe
csv_path = 'vehicles_us.csv'
if os.path.exists(csv_path):
    st.success(f"Archivo '{csv_path}' encontrado")
    
    # Intentar cargar
    try:
        car_data = pd.read_csv(csv_path)
        st.write(f"Datos cargados: {len(car_data)} filas")
        st.dataframe(car_data.head())
    except Exception as e:
        st.error(f"Error al cargar: {e}")
else:
    st.error(f"Archivo '{csv_path}' NO encontrado")
    
    # Mostrar ruta absoluta para debug
    st.write(f"Directorio actual: {os.path.abspath('.')}")
