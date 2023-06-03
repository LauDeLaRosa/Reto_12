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


