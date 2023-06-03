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
