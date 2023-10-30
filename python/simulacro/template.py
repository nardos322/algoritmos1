# Ejercicio 1
#
#  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
#    requiere: {e pertenece a s }
#    asegura: {res es la posición de la última aparición de e en s}
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,100,0,100,0,-1,-1]
#   e = 0
# se debería devolver res=7

def pertenece(l: list, n: int) -> bool:

    for i in range(len(l)):
        if l[i] == n:
            return True
        
    return False


def ultima_aparicion(s: list, e: int) -> int:
    #itero pero para atras
    for i in range(len(s)-1,-1,-1):
        if s[i] == e:
            return i
        





##########################################################################
##########################################################################

# Ejercicio 2
#
#  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
#    requiere: -
#    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
#    asegura: {res no tiene elementos repetidos }
#  }

# Por ejemplo, dados
#   s = [-1,4,0,4,3,0,100,0,-1,-1]
#   t = [0,100,5,0,100,-1,5]
# se debería devolver res = [3,4,5] ó res = [3,5,4] ó res = [4,3,5] ó res = [4,5,3] 
# ó res = [5,3,4] ó res = [5,4,3]

def quitar_repetidos(s: list) -> list:
    res: list = []
    for i in range(len(s)):
        if not pertenece(res, s[i]):
            res.append(s[i])
    return res

    

def elementos_exclusivos(s: list, t: list) -> list:
    res: list = []
    # agrego a res los elementos de s que no pertenecen a t
    for i in range(len(s)):
        
        if not (pertenece(t, s[i])):
            res.append(s[i])
    # agrego a res los elementos de t que no pertenecen a s
    for j in range(len(t)):
        if not (pertenece(s, t[j])):
            res.append(t[j])
    
    # como res puede tener numeros repetidos se los quito
    res = quitar_repetidos(res)

    return res       
   



##########################################################################
##########################################################################

# Ejercicio 3
#
# Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
# en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
# en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
# palabras que tienen la misma traducción en inglés y en alemán.

#  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
#    requiere: -
#    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
#  }

#  Por ejemplo, dados los diccionarios
#    aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#    inglés = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#  se debería devolver res=2

aleman = {"Mano": "Hand", "Brazo": "Arm", }
ingles = {"Pie": "Foot", "Mano": "Hand","Brazo": "Arm"}


def contar_traducciones_iguales(ingles: dict, aleman: dict) -> int:
    res: list = []
    contador: list = 0
    
    for i in ingles:
        if i in aleman and ingles[i] == aleman[i]:
            contador +=1
    
    return contador        


print(contar_traducciones_iguales({},{}))

##########################################################################
##########################################################################

# Ejercicio 4
#
# Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
# y sus valores la cantidad de veces que cada uno de esos números aparece en s

#  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
#    requiere: -
#    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
#  }

#  Por ejemplo, dada la lista
#  lista = [-1,0,4,100,100,-1,-1]
#  se debería devolver res={-1:3, 0:1, 4:1, 100:2}
#  
# RECORDAR QUE NO IMPORTA EL ORDEN DE LAS CLAVES EN UN DICCIONARIO

lista = [-1, 0, 4, 100, 100, -1, -1] 

def convertir_a_diccionario(lista: list) -> dict:
    res: dict = {}

    for i in lista:
        if not i in res:
            res[i] = 1
        else:
            res[i] +=1
    return res


        