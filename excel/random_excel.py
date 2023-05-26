import pandas as pd
import random

# Leer el archivo de Excel
df = pd.read_excel('path/file.xlsx')

# Mezclar aleatoriamente las filas
filas_aleatorias = df.sample(frac=1, random_state=42)  # Utiliza random_state para obtener resultados reproducibles

# Guardar las filas aleatorias en un nuevo archivo de Excel
filas_aleatorias.to_excel('path/newfile.xlsx', index=False)
