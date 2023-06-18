from typing import List
from typing import Dict
import json

# x = [{'a':'1','b':'2','d':'7'},{'a':'3','c':'4'},{'a':'6'}]
# y = {}


def unir_diccionarios(a_unir: List[Dict[str,int]]) -> Dict[str,List[str]]:
  # Implementar esta funcion
  t = {}

  for i in a_unir:
  
   for j in i:
    
    if not j in t:
    
      t[j] = [i[j]]
    else:
      t[j].append(i[j])  

  return t



# print(unir_diccionarios(x))


    

  



if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))