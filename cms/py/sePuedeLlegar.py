from typing import List
from typing import Tuple


vuelos: List[Tuple[str, str]] = [('C','D'),('F','G'),('G','A'),('D','F')]

origen: str = 'C'
destino: str = 'A'


def ordenar_vuelos(origen: str, vuelos: List[Tuple[str, str]]) -> List[Tuple[str,str]]:
  vuelos_ord: List[Tuple[str,str]] = []

  vuelos_res = vuelos.copy()
  continuar: bool = True
  ciudad_buscada = origen

  while continuar:
    for i in range(len(vuelos)):
      if len(vuelos_res) == 0:
        return vuelos_ord
      vuelo = vuelos[i]
      if vuelo[0] == ciudad_buscada:
        vuelos_ord.append(vuelo)
        vuelos_res.remove(vuelo)
        ciudad_buscada = vuelo[1]
        
    continuar = False

    for i in range(len(vuelos_res)):
      if vuelos_res[i][0] == ciudad_buscada:
        continuar = True
  return vuelos_ord



def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  # definir esta función

 
  vuelos_ord = ordenar_vuelos(origen, vuelos)
  if len(vuelos_ord) == 0: return -1

  for i in range(len(vuelos_ord)):
    if vuelos_ord[i][1] == destino:
      return i+1
  return -1  
        

print(sePuedeLlegar(origen, destino, vuelos))
   

# if __name__ == '__main__':
#   origen = input()
#   destino = input()
#   vuelos = input()
  
#   print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))              