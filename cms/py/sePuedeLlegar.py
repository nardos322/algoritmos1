from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

vuelos: List[Tuple[str, str]] = [('A','B'),('B','E'),('E','C')]
contador_de_vuelos: int = 0
destinos_vuelos: List[str] = []
origen_vuelos: List[str] = []
rutas: List[Tuple[str, str]] = []

origen: str = 'A'
destino: str = 'E'


def pertenece(lista: list, n: float) -> bool:
    for numero in lista:
        if(numero == n):
            return True
        
    return False






def soloParteUnVueloDeCadaCiudad(vuelos: List[Tuple[str,str]]) -> bool:
  for i in range(len(vuelos)):
    origen_vuelos.append(vuelos[i][0])
  for destino in origen_vuelos:
    if(origen_vuelos.count(destino)>1):
      return False
  return True  

def soloLlegaUnVueloAcadaCiudad(vuelos: List[Tuple[str,str]]) -> bool:
  
  for i in range(len(vuelos)):
    destinos_vuelos.append(vuelos[i][1])
  for destino in destinos_vuelos:
    if(destinos_vuelos.count(destino)>1):
      return False
  return True  

  
def hayRuta(vuelos: List[Tuple[str, str]], origen: str, destino: str) -> bool:
  hay_origen: bool = False
  hay_destino: bool = False
  
  for ruta_origen in vuelos:
   
    if((ruta_origen[0] == origen)):
      hay_origen = True
   
  for ruta_destino in vuelos:
    if(ruta_destino[1] == destino):
      hay_destino = True  
    
  if(hay_origen and hay_destino):
    return True
  else:
    return False    

def caminoDeVuelos(vuelos: List[Tuple[str,str]]):
  for i in range(1,len(vuelos)):
    if not vuelos[i][0] == vuelos[i-1][1]:     
      return False
  return True  




def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  # definir esta función
  if(hayRuta(vuelos, origen, destino)):
    for ruta in vuelos:
      
      if(ruta[0]== origen) or (ruta[1] == destino):
        
        rutas.append(ruta)
         
    if(caminoDeVuelos(rutas)):
      return len(rutas)
    else:
      return -1    
    

ruta1 =  [('A','B')]

ruta2 = ('B','E')
   
print(pertenece(ruta1[0], ruta2[0]))

#print(soloLlegaUnVueloAcadaCiudad(vuelos))
#print(soloParteUnVueloDeCadaCiudad(vuelos))
#print(caminoDeVuelos(vuelos))
#print(hayRuta(vuelos, origen, destino))
print(sePuedeLlegar(origen, destino, vuelos))

# if __name__ == '__main__':
#   origen = input()
#   destino = input()
#   vuelos = input()
  
#   print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))