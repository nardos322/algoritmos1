def pertenece(lista: list, n: float) -> bool:
    for numero in lista:
        if(numero == n):
            return True
        
    return False

def pertenece2(lista: list, n: float) -> bool:
    i: int = 0
    while i < len(lista):
        if(lista[i] == n): 
            return True
        i += 1
    return False


def pertenece3(lista: list, n: float) -> bool:
    if len(lista) == 0:
        return False
    
    if(lista[0] == n):
        return True
    elif(lista[0] != n):
        lista.pop(0)
        return pertenece3(lista, n)
    

  
    
def divide_a_todos(numeros: list, n: float) -> bool:
    valor: bool 
    for numero in numeros:
        if(numero%n != 0):
            return False
        else:
            valor = True        
    return valor

def suma_total(s: list) -> float:
    suma: float = 0
    for i in range(len(s)):
        suma += s[i]
    return suma


def ordenados(s: list) -> bool:
    
    for i in range(len(s)):
        if(s[0] < s[i] < s[len(s)-1]):
            return True
    return False


def tiene_mas_de7(p: str) -> bool:
    return len(p) > 7


def es_palindromo(palabra: str) -> bool:
    
    i: int = len(palabra) - 1
    p_invertida: str = ''

    while i >= 0:
        p_invertida += palabra[i]
         
        i -= 1        
    return palabra == p_invertida
 




print(es_palindromo('reconocer'))