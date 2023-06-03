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
