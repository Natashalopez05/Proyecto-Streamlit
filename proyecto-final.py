import numpy as np
import streamlit as st
import pandas as pd
import os
from math import e
from re import T
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MultiLabelBinarizer
from mymodel import load_model, predict_genres

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_files(directory):
    if not os.path.exists(directory):
        return []
    else:
        return [f for f in os.listdir(directory) if f.endswith('.csv')]
    
def process_csv(selected_file):
    # Leer el archivo CSV
    df = pd.read_csv(selected_file)

    # Mostrar el numero de filas y columnas
    st.write('Numero de filas:')
    st.write(f"Filas: {df.shape[0]}")
    st.write(f"Columnas: {df.shape[1]}")

    # Mostrar el DataFrame
    st.write("Datos del archivo CSV seleccionado:")
    st.write(df)

def process_csv_files(directory, title):
    st.subheader(title)
    create_dir(directory)
    files = get_files(directory)
    selected_file = st.selectbox(f"Selecciona un archivo CSV en '{directory}':", files)
    if selected_file:
        process_csv(os.path.join(directory, selected_file))

st.title('Clasificación de Información', anchor='center')

model, mlb, vectorizer = load_model('./models/model.pkl', './models/mlb.pkl', './models/vectorizer.pkl')
busqueda = st.text_input('Introduce una frase:', key='test_sentence')
predicted_genres = predict_genres(busqueda, model, mlb, vectorizer)

if busqueda:
    st.write(f"Oración de prueba: '{busqueda}'")
    st.write(f"Géneros predichos: '{predicted_genres}'")

process_csv_files('_split_csv', 'Archivos CSV Originales')
process_csv_files('_clean_csv', 'Archivos CSV Limpios')


