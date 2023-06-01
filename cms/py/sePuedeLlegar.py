from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

vuelos = [('A','B'),('B','E'),('E','F')]

origen = 'A'
destino = 'F'


def pertenece(lista: list, n: float) -> bool:
    for numero in lista:
        if(numero == n):
            return True
        
    return False



def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  # definir esta función
  for i in range(len(vuelos)):
    #print(i)
    if(pertenece(vuelos[i], origen)):
       print(vuelos[i][1])
    
 



sePuedeLlegar(origen, destino, vuelos)

# if __name__ == '__main__':
#   origen = input()
#   destino = input()
#   vuelos = input()
  
#   print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))