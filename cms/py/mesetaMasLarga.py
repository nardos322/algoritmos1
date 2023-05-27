from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  
  values: List[int] = []
  contador: int = 0

  if l == []:
    return 0

  if todos_distintos(l):
    return 1
 
  for i in range(len(l)):
    
    if i < len(l)-1 :
      if l[i] == l[i+1]:
        contador += 1
        #values.append(l[i])
        #print(1, values)
      elif l[i] != l[i+1] and l[i+1] == len(l)-1:
        return contador + 1  
      else:
        contador = 0
        
  
  #return secuencia_de_repetidos(values)
  return contador + 1
  
                    

def todos_distintos(l: List[int]) -> bool:

  value: bool
  if len(l) == 1 :
    return True
  for i in range(len(l)):
    if i < len(l)-1:
      if l[i] != l[i+1]:
        value = True
      else:
        return False
 
  return value 




def secuencia_de_repetidos(l: List[int]) -> int:
  contador: int = 0
  meseta: List[int] = []
  
  for i in range(len(l)):
    if i < len(l)-1 and l[i] == l[i+1]:
      contador += 1
    else:
      meseta.append(contador + 1)
      contador = 0
  return max(meseta) + 1
    
     
print(mesetaMasLarga([1,1,3]))        



# if __name__ == '__main__':
#   x = input()
#   print(mesetaMasLarga([int(j) for j in x.split()]))