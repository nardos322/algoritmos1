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


# Ejercicio 5

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
    

# def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int) -> int:
#     if(n%3 == 0):
#         return n*2
#     elif(n%9 == 0):
#         return n*3
#     else:
#         return n

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(n: int) -> int:
    if(n%3 == 0):
        return n*2
    if(n%9 == 0):
        return n*3
    else:
        return n    
    
def tu_nombre(nombre: str) -> str:
    if len(nombre) >= 5:
        return 'Tu nombre tiene muchas letras'
    else:
        return 'Tu nombre tiene menos de 5 caracteres'
        
def vas_de_vacaciones_o_te_toca_trabajar(sexo: str, edad: int) -> str:
    if(sexo == 'm' and edad >= 65) or (sexo == 'f' and edad >= 60):
        return 'Anda de vacaciones'
    elif(sexo == 'm' and edad >= 18 and edad < 65) or (sexo == 'f' and edad >=18 and edad < 60):
        return 'te toca ir a trabajar'        
    else:
        return 'anda de vacaiones'
    
# Ejercicio 6    

def imprimir_10veces() -> int:
    i: int = 0
    while i<=10:
        print(i)
        i+=1

def imprimir_pares() -> int:
    i: int = 10
    while i<=40:
        print(i)
        i+=2

def imprimir_eco() -> str:
    i: int = 0
    while i<10:
        print('eco')
        i+=1

def iniciar_despegue(n: int) -> str:
    i: int = 0
    while i<n:
        print(n)
        n-=1
    print('Despegue!')   


def viaje_en_el_tiempo(año_partida: int, año_llegada: int) -> str:
    i: int = 1
    if(año_partida<año_llegada):
        print('El año de partida tiene que se mayor al de llegada')
    while año_llegada < año_partida:
        print(f"viajo {i} años al pasado estamos en {año_partida-1}")
        año_partida-=1
        i+=1    



def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0

def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g



print(ro(1))
print(ro(1))
print(ro(1))

print(rt(1, 0))
print(rt(1, 0))
print(rt(1, 0))