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
    x: int = 0
    for i in range(len(s)):
        print(s[i])

ordenados([1,2,3])