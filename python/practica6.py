import math


def imprimir_hola_mundo()-> str:
    print("hola mundo")
    
def imprimir_un_verso()-> str:
    print("quiero la libertadores\ny una gallina matar")
    
def raizDe2() -> float:
    res: float = round(math.sqrt(2), 4)
    return res 


def factorial_de_dos()-> int:
    res: int = 2*1
    return res

def perimetro()-> float:
    res: float = 2*math.pi
    return res


def imprimir_saludo(name: str) -> str:
    res: str = f"hola {name}"
    print(res)


def raiz_cuadrada_de(n: float) -> float:
    res: float = math.sqrt(n)
    return res


def fahrenheit_a_celsius(n: float) -> float:
    res: float = round(((n-32)*5)/9)
    return res

def imprimir_dos_veces(estribillo: str) -> str:
    print(estribillo*2)
    
def es_multiplo_de(x: int, y: int) -> bool:
    return x%y == 0    

def es_par(n: int) -> bool:
    return es_multiplo_de(n, 2)


def cantidad_de_pizzas(comensales: int, min_cant_porciones: int) -> int:
    if (comensales*min_cant_porciones) < 8:
        return 1
    return ((comensales*min_cant_porciones)//8) + 1


def alguno_es_0(n1: int, n2: int) -> bool:
    return n1 == 0 or n2 == 0


def ambos_son_0(n1: int, n2: int) -> bool:
    return n1 == 0 and n2 == 0


def es_nombre_largo(name: str) -> bool:
    return len(name) >= 3 and len(name) <= 8

def es_bisiesto(year: int) -> bool:
    return year%4 == 0 and not(year%100 == 0)

def peso_pino(altura: int) -> int:
    peso: int = 0
    for i in range(1,altura+1):
       
       if i <= 3:
           peso = i*100 * 3
       else:
           peso += 1*100 * 2
    return peso      


def es_peso_util(peso: int) -> bool:
    return peso >= 400 and peso <=1000   

def sirve_pino(altura: int) -> bool:
    return es_peso_util(peso_pino(altura))


def es_nombre_largo(name: str) -> bool:
    return len(name) >= 3 and len(name) <= 8


def devolver_el_doble_si_es_par(n: int) -> int:
    if(n%2 == 0):
        return n*2
    else:
        return n
    
def devolver_el_valor_si_es_par_sino_el_que_sigue(n: int) -> int:
    if(n%2 == 0):
        return n
    else:
        return n+1   

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int) -> int:
    if(n%3 == 0):
        return n*2
    if(n%9 == 0):
        return n*3
    else:
        return n    
        
 
def lindo_nombre(name: str) -> str:
    if len(name) >= 5:
        return "tu nombre tiene muchas letras"
    else:
        return "tu nombre tiene menos de 5 caracteres"

def el_rango(n: int) -> int:
    if n < 5:
        print("el numero es menor a 5")
    elif n>=10 and n<=20:
        print("el numero esta entre 10 y 20")
    elif n>20:
        print("el numero es mayor a 20")


def vas_de_vacaciones_o_te_toca_trabajar(sexo: str, edad: int) -> str:
    if(sexo == 'm' and edad >= 65) or (sexo == 'f' and edad >= 60):
        return 'Anda de vacaciones'
    elif(sexo == 'm' and edad >= 18 and edad < 65) or (sexo == 'f' and edad >=18 and edad < 60):
        return 'te toca ir a trabajar'        
    else:
        return 'anda de vacaiones'                




def imprimir_10veces() -> int:
    i: int = 10
    for i in range(1,i+1):
        print(i)

def imprimir_pares_10_40() -> int:
    i: int = 40
    for i in range(2,i+2,2):
        print(i)
        
def imprimir_10_eco()-> str:
    n: int = 0
    for n in range(n,10):
        print(n,"eco")

            


def cuenta_regresiva(n: int) -> str:
    
    while n>=1:
        print(n)
        n -= 1        
    print("Despegue!")    

def cuenta_regresiva_for(n: int) -> str:
    for i in range(0,n,1):
        print(n-i)
    print("Despegue!")


def cuenta_regresiva_for2(n: int) -> str:
    for i in range(n,0,-1):
        print(i)
    print("Despegue!")

def viaje_en_el_tiempo(año_partida: int, año_llegada: int) -> str:
    i: int = 1
    while año_partida > año_llegada:
       
        if(i == 1):
            print(f"viajaste {i} año en el tiempo, estamos en el año {año_partida-1}")
            año_partida -= 1
            i += 1
        print(f"viajaste {i} años en el tiempo, estamos en el año {año_partida-1}")
        año_partida -= 1
        i += 1

def viaje_aristoteles(año_partida: int)-> str:
        año_aristoteles: int = -384
        i:int = 20
        while not(año_partida <= año_aristoteles):
            
            
            print(f"viajaste {i} años en el tiempo, estamos en el año {año_partida-20}")
            año_partida -= 20
            i += 20


