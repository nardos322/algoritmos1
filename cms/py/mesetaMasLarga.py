from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  count: int = 0
  

def todosIguales(l: List[int],i: int,j: int) -> bool:
  k:int = 0
  count: int = 0
  while i<= k < j:
    if l[k] == l[i]:
      count += 1
    elif l[k] == l[i+1]: 
      
      count += 1
      
    k+=1  
  return count  

 
    


print(todosIguales([1,2,2,2],0, 4))

# if __name__ == '__main__':
#   x = input()
#   print(mesetaMasLarga([int(j) for j in x.split()]))