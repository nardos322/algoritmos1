def pertenece(n: float, lista: list) -> bool:
    for numero in lista:
        print(numero)
        if(numero == n):
            return True
        
    return False

def contar_lineas(nombre_archivo: str) -> int:
    archivo: str = open(nombre_archivo, 'w')
    archivo = archivo.readlines()
    archivo.close()

    return len(archivo)




def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    archivo: str = open(nombre_archivo)
    archivo = archivo.readlines()
    
    
        
    
    
    

print(existe_palabra('¡Bienvenide!\n','text.txt'))

