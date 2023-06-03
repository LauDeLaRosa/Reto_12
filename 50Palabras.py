from collections import Counter
import re

def obtener_palabras_mas_comunes(archivo):
    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leer el contenido del archivo
            contenido = file.read()
            
            # Utilizar expresión regular para dividir el contenido en palabras
            palabras = re.findall(r'\w+', contenido.lower())
            
            # Calcular la frecuencia de las palabras
            frecuencia_palabras = Counter(palabras)
            
            # Obtener las 50 palabras más comunes en orden descendente de frecuencia
            palabras_comunes = frecuencia_palabras.most_common(50)
            
            # Devolver el listado de palabras más comunes
            return palabras_comunes
    
    except FileNotFoundError:
        print("El archivo no existe.")

# Prueba del código
archivo_txt = 'C:\\Users\\jaide\\Documents\\LAURA DE LA ROSA U\\Reto 12\\mbox-short.txt' 
palabras_mas_comunes = obtener_palabras_mas_comunes(archivo_txt)

print("Listado de las 50 palabras más repetidas:")
for palabra, frecuencia in palabras_mas_comunes:
    print(f"{palabra}: {frecuencia}")
