# Reto_12
## Punto 1
### endswith
Determina si una cadena de texto termina con los caracteres de una cadena indicada, devolviendo true o false según corresponda.
### startswith
Indica si una cadena de texto comienza con los caracteres de una cadena de texto concreta, devolviendo true o false según corresponda.
### isalpha
Devuelve True si todos los caracteres de la cadena son alfabetos. Si no es así, devuelve False.
### isalnum
Devuelve True si todos los caracteres de la cadena son alfanuméricos (alfabetos o números). Si no es así, devuelve False.
### isdigit
El método devuelve True si todos los caracteres de una cadena son dígitos. Si no, devuelve False.
### isspace
Devuelve True si sólo hay caracteres de espacio en blanco en la cadena. Si no, devuelve False.
### istitle
Devuelve True si la cadena es una cadena con mayúsculas y minúsculas. Si no es así, devuelve False.
### islower
Devuelve True si todos los alfabetos de una cadena son alfabetos en minúsculas. Si la cadena contiene al menos un alfabeto en mayúsculas, devuelve False.
### isupper
Devuelve si todos los caracteres de una cadena están en mayúsculas o no.

## Punto 2
Procesar el archivo y extraer:
### Cantidad de vocales
```python
def contar_vocales(archivo):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # Se definen las vocales en mayúsculas y minúsculas
    
    # Inicializar el contador de vocales
    contador = 0
    
    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leer el contenido del archivo
            contenido = file.read()
            
            # Recorrer cada carácter en el contenido
            for caracter in contenido:
                # Verificar si el carácter es una vocal
                if caracter in vocales:
                    contador += 1
    
    except FileNotFoundError:
        print("El archivo no existe.")
    
    # Devolver la cantidad de vocales encontradas
    return contador

# Prueba del código
archivo_txt = 'C:\\Users\\jaide\\Documents\\LAURA DE LA ROSA U\\Reto 12\\mbox-short.txt'
cantidad_vocales = contar_vocales(archivo_txt)
print(f"La cantidad de vocales en el archivo es: {cantidad_vocales}")
```
### Cantidad de consonantes
```python
def contar_consonantes(archivo):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']     # Se definen las vocales en mayúsculas y minúsculas
    
    # Inicializar el contador de consonantes
    contador = 0
    
    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leer el contenido del archivo
            contenido = file.read()
            
            # Recorrer cada carácter en el contenido
            for caracter in contenido:
                # Verificar si el carácter no es una vocal y es una letra
                if caracter.isalpha() and caracter not in vocales:
                    contador += 1
    
    except FileNotFoundError:
        print("El archivo no existe.")
    
    # Devolver la cantidad de consonantes encontradas
    return contador

# Prueba del código
archivo_txt = 'C:\\Users\\jaide\\Documents\\LAURA DE LA ROSA U\\Reto 12\\mbox-short.txt'  
cantidad_consonantes = contar_consonantes(archivo_txt)
print(f"La cantidad de consonantes en el archivo es: {cantidad_consonantes}")
```
### Listado de las 50 palabras que más se repiten
```python
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
```
### Listado de destinatarios con cantidad de mensajes recibidos
```python
def obtener_destinatarios_mensajes(archivo):
    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leer el contenido del archivo
            contenido = file.readlines()
            
            # Inicializar el diccionario para almacenar destinatarios y su cantidad de mensajes
            destinatarios = {}
            
            # Recorrer cada línea del contenido
            for linea in contenido:
                # Dividir la línea en destinatario y mensaje
                partes = linea.split(':')
                
                if len(partes) == 2:
                    destinatario = partes[0].strip()
                    
                    # Verificar si el destinatario ya existe en el diccionario
                    if destinatario in destinatarios:
                        destinatarios[destinatario] += 1
                    else:
                        destinatarios[destinatario] = 1
    
    except FileNotFoundError:
        print("El archivo no existe.")
    
    # Devolver el diccionario de destinatarios y cantidad de mensajes
    return destinatarios

# Prueba del código
archivo_txt = 'C:\\Users\\jaide\\Documents\\LAURA DE LA ROSA U\\Reto 12\\mbox-short.txt'  
destinatarios_mensajes = obtener_destinatarios_mensajes(archivo_txt)

print("Listado de destinatarios y cantidad de mensajes recibidos:")
for destinatario, cantidad_mensajes in destinatarios_mensajes.items():
    print(f"Destinatario: {destinatario} - Cantidad de mensajes: {cantidad_mensajes}")
```
### Cantidad de mensajes enviados por cada día
```python
from collections import defaultdict
from dateutil.parser import parse

def obtener_cantidad_mensajes_por_dia(archivo):
    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r') as file:
            # Leer el contenido del archivo
            contenido = file.readlines()
            
            # Inicializar el diccionario para almacenar las fechas y la cantidad de mensajes
            mensajes_por_dia = defaultdict(int)
            
            # Recorrer cada línea del contenido
            for linea in contenido:
                # Dividir la línea en fecha y mensaje
                partes = linea.split(',')
                
                if len(partes) == 2:
                    fecha_str = partes[0].strip()
                    mensaje = partes[1].strip()
                    
                    try:
                        # Convertir la cadena de fecha a objeto de fecha utilizando dateutil.parser.parse
                        fecha = parse(fecha_str).date()
                        
                        # Incrementar la cantidad de mensajes para la fecha correspondiente
                        mensajes_por_dia[fecha] += 1
                    except ValueError:
                        # Si no se puede analizar la fecha, continuar con la siguiente línea
                        continue
    
    except FileNotFoundError:
        print("El archivo no existe.")
    
    # Devolver el diccionario de fechas y cantidad de mensajes
    return mensajes_por_dia

# Prueba del código
archivo_txt = 'C:\\Users\\jaide\\Documents\\LAURA DE LA ROSA U\\Reto 12\\mbox-short.txt'  
cantidad_mensajes_por_dia = obtener_cantidad_mensajes_por_dia(archivo_txt)

print("Cantidad de mensajes enviados por día:")
for fecha, cantidad_mensajes in cantidad_mensajes_por_dia.items():
    print(f"Fecha: {fecha} - Cantidad de mensajes: {cantidad_mensajes}")
```








