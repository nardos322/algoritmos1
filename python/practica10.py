

def pertenece(n: float, lista: list) -> bool:
    for numero in lista:
        
        if(numero == n):
            return True
        
    return False

def contar_lineas(nombre_archivo: str) -> int:
    archivo: str = open(nombre_archivo, 'w')
    archivo = archivo.readlines()
    archivo.close()

    return len(archivo)




def existe_palabra(palabra_input: str, nombre_archivo: str) -> bool:
    palabras_sin_tildes = []
    archivo_limpio: list = []
    text = ''
    archivo: str = open(nombre_archivo)
    archivo = archivo.readlines()

    for linea in archivo:
        archivo_limpio.append(linea.replace('\n',''))

    for linea in archivo_limpio:
        text += linea

    text = text.replace('!',' ')    
    text = text.replace('¡','') 
    text = text.replace('/', ' ')   
    text = text.replace('(', '')
    text = text.replace(')','')
    text = text.replace(':',' ')
    text = text.replace('.',' ')
    text = text.replace('#', '')
    text = text.lower()
    separado_en_palabras = text.split()

    for palabra in separado_en_palabras:
        
        if(pertenece('á',palabra) or pertenece('é',palabra) or pertenece('í',palabra) or pertenece('ó',palabra) or pertenece('ú',palabra)):
            
            if pertenece('á',palabra):
                palabra_sin_tilde = palabra.replace('á', 'a')
                palabras_sin_tildes.append(palabra_sin_tilde)
            elif pertenece('é',palabra):
                palabra_sin_tilde = palabra.replace('é','e')
                palabras_sin_tildes.append(palabra_sin_tilde)
            elif pertenece('í',palabra):
                palabra_sin_tilde = palabra.replace('í','i')
                palabras_sin_tildes.append(palabra_sin_tilde)
            elif pertenece('ó',palabra):
                palabra_sin_tilde = palabra.replace('ó','o')
                palabras_sin_tildes.append(palabra_sin_tilde)
            elif pertenece('ú',palabra):
                palabra_sin_tilde = palabra.replace('ú','u')
                palabras_sin_tildes.append(palabra_sin_tilde)
           
        elif not(pertenece('á',palabra) or pertenece('é',palabra) or pertenece('í',palabra) or pertenece('ó',palabra) or pertenece('ú',palabra)):
            
            palabras_sin_tildes.append(palabra)

    return pertenece(palabra_input, palabras_sin_tildes)     
   
    
   



