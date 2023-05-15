import math

# ejercicio1

def raizDe2()-> float:
    res: float = round(math.sqrt(2), 4)
    return res 

def imprimir_hola()-> str:
    res: str =  'holaa'
    print(res)

def imprimir_verso()-> str:
    res: str = 'dale campeeon \ndale campeon'
    print(res)

def factorial_de_dos()-> int:
    res = 2*1
    return res

def factorial_de_3()-> int:
    res = 3*2*1
    return res 

def factorial_de_4()-> int:
    res = 4*3*2*1
    return res 

def factorial_de_5()-> int:
    res = 5*4*3*2*1
    return res

def factorial_de(n: int) -> int:
    y: int = 1
    for i in range(1, n+1):
        y = y * i
    return y

def fact_recursivo(x: int) -> int:
    if x == 0:
        return 1
    else:
        return x*fact_recursivo(x-1)


# Ejercicio 2

def imprimir_saludo(name: str) -> str:
    res: str = f"hola {name}"
    print(res)

def raiz_cuadrada_de(n: int)-> int:
    res: int = math.sqrt(n)
    return res


def imprimir_dos_veces(estribillo: str) -> str:
    print(estribillo*2)

def es_multiplo_de(x: int, y: int) -> bool:
    return x%y == 0

def es_par(n: int) -> bool:
    return es_multiplo_de(n, 2)


# Ejercicio 3

def alguno_es_0(n1: int, n2: int) -> bool:
    return n1 == 0 or n2 == 0


def ambos_son_0(n1: int, n2: int) -> bool:
    return n1 == 0 and n2 == 0


def es_nombre_largo(name: str) -> bool:
    return len(name) >= 3 and len(name) <= 8

def es_bisiesto(year: int) -> bool:
    return year%4 == 0 and not(year%100 == 0)


# Ejercicio 4

def peso_pino(altura: int) -> int:
    peso: int = 0
    for i in range(1, altura+1):
       peso += i
    return peso
        
    