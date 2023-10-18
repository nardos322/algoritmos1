
def pertenece(l: list, n: int) -> bool:

    for i in range(len(l)):
        if l[i] == n:
            return True
        
    return False


def divide_a_todos(l: list, n: int) -> bool:

    for numero in l:
        if not(numero%n == 0):
            return False
    return True    


def suma_total(l: list) -> int:
    res: int = 0

    for n in l:
        res += n
    return res   

def ordenados(l: list) -> bool:
    
    
    for i in range(len(l)-1):
        if not(l[i] < l[i+1]):
            return False
    return True    
    
def hay_palabra_mayor_a_7(palabras: list) -> bool:

    for palabra in palabras:
        if len(palabra) > 7:
            return True
    return False    





def es_palindromo(palabra: str) -> bool:
    
    i: int = len(palabra) - 1
    p_invertida: str = ''

    while i >= 0:
        
        p_invertida += palabra[i]
        i -= 1
    palabra = formatear_texto(palabra)
    p_invertida = formatear_texto(p_invertida)        
    return palabra == p_invertida


def formatear_texto(text: str) -> str:
    text_format = text
    
    text_format = text_format.replace('á', 'a')
    text_format = text_format.replace('é', 'e')
    text_format = text_format.replace('í', 'i')
    text_format = text_format.replace('ó', 'o')
    text_format = text_format.replace('ú', 'u')
    text_format = text_format.replace(' ','')
    text_format = text_format.lower()
    
    return text_format     



def borrar_repetidos(s: list):
    res: list = []
    print("hola")
    for i in range(len(s)):
        if not pertenece(res, s[i]):
            res.append(s[i])
    return res        

def mis_estudiantes():
   
    name = " "

    mis_estudiantes: list = []

    while not (name == "listo"):
        name: str = input('nombre de estudiantes: ')
        if name == "listo":
            return mis_estudiantes
        mis_estudiantes.append(name)
        
   
def pertenece_a_cada_uno(s: list, elem: int) -> list:

    res = []
    for sublista in s:
        if pertenece(sublista, elem):
            res.append(True)
        else:
            res.append(False)    
    return res


def es_matriz(s: list) -> bool:
    
    inicio: int = len(s[0]) 
    for i in range(len(s)):
        if inicio != len(s[i]):
            return False
    return True    
    


def filas_ordenadas(s: list) -> list:
    res = []
    for i in s:
        if ordenados(i):
            res.append(True)
        else:
            res.append(False)
    return res



