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
