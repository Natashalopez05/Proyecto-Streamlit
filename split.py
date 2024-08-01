import pandas as pd
import os


def split_csv(file_path, chunk_size, output_directory):

    """divide un archivo CSV en varios archivos más pequeños y los guarda como archivos CSV separados en un directorio especifico
    
    :param file_path: Ruta al archivo CSV original.
    :param chunk_size: Numero de filas por archivo.
    :param output_directory: Directorio para guardar los archivos dividios
    """
   
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    chunks = pd.read_csv(file_path, chunksize=chunk_size)

    for i, chunk in enumerate(chunks):
      output_file = os.path.join(output_directory, f"archivo_dividido_parte_{i+1}.csv")
      chunk.to_csv(output_file, index=False)
      print(f"Guardando {output_file}...")

# Parametros
file_path = 'df_final.csv'
chunk_size = 10000
output_directory = '_clean_csv'

# Dividir el archivo CSV
split_csv(file_path, chunk_size, output_directory)