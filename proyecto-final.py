from math import e
import streamlit as st
import pandas as pd
import os
st.title('Clasificación de Información', anchor='center')

# Funcion para procesar archivos CSV
def process_csv(directory):
    if not os.path.exists(directory):
        st.error(f'El directorio {directory} no existe.')
    else: 
        # Obtener la lista de archivos CSV en el directorio
        files = [f for f in os.listdir(directory) if f.endswith('.csv')]

        if not files:
            st.warning(f'No se encontraron archivos CSV en el directorio "{directory}".')
        else: 
            # Mostrar el selector de archivos
            selected_file = st.selectbox(f"Selecciona un archivo CSV en '{directory}':", files)

            if selected_file:
                file_path = os.path.join(directory, selected_file)

                try:
                    # Leer el archivo CSV
                    df = pd.read_csv(file_path)

                    # Verificar si el DataFrame esta vacio
                    if df.empty:
                        st.warning('El archivo CSV esta vacio.')
                    else:

                        # Mostrar el numero de filas y columnas
                        st.write('Numero de filas:')
                        st.write(f"Filas: {df.shape[0]}")
                        st.write(f"Columnas: {df.shape[1]}")

                        # Mostrar el DataFrame
                        st.write("Datos del archivo CSV seleccionado:")
                        st.write(df)

                except Exception as e:
                    st.error(f'Error al leer el archivo CSV: {e}')

# Procesar los directorios

st.subheader('Archivos CSV Originales')
process_csv('split_csv')

st.subheader('Archivos CSV Limpios')
process_csv('clean_csv')