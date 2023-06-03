from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

vuelos: List[Tuple[str, str]] = [('J','C'),('A','R'),('B','E'),('R','J')]
rutas: List[Tuple[str, str]] = []

origen: str = 'A'
destino: str = 'C'


  
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
  ciudad_buscada: str 
  continuar = True
  for ruta in vuelos:
    if ruta[0] == origen and ruta[1] == destino:
      return 1

  if(hayRuta(vuelos, origen, destino)):
    for ruta in vuelos:
      
      if ruta[0] == origen :
        rutas.append(ruta)
        vuelos.remove(ruta)  
        ciudad_buscada = ruta[1]
      
    while continuar:
      for ruta in vuelos:  
        
        if ruta[0] == ciudad_buscada:
          print(ciudad_buscada)
          rutas.append(ruta)  
          
          ciudad_buscada = ruta[1]
          
          
          if hayRuta(rutas, origen, destino) and caminoDeVuelos(rutas):
            
            return len(rutas) 
          
          continuar = False
       
      for i in range(len(vuelos)):
        print(rutas)
        if not vuelos[i][0] == ciudad_buscada:
          continuar = False
        elif vuelos[i][0] == ciudad_buscada:
          
          continuar = True
        
   
    if(hayRuta(rutas, origen, destino) and caminoDeVuelos(rutas)):
      
      return len(rutas)
    else: 
     
      return -1
    
  else:
    return -1

  

print(sePuedeLlegar(origen, destino, vuelos))    




# if __name__ == '__main__':
#   origen = input()
#   destino = input()
#   vuelos = input()
  
#   print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))