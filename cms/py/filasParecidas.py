from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def filasParecidas(matriz: List[List[int]]) -> bool :
  # Implementar esta funcion
  for n in range(-10, 10):
    res: bool = filasParecidasAanterior(matriz, n)
    if(res == True):
      return res
    else:
      return False
  

def filasParecidasAanterior(matriz: List[List[int]], n: int):
  if(len(matriz) == 1):
     return True
  
  for i in range(1,len(matriz)):
    
    res = filaAnteriorMasN(matriz, i, n)
  return res

def filaAnteriorMasN(matriz: List[List[int]], i: int, n: int):

  for j in range(len(matriz[0])):
      if(matriz[i][j] == (matriz[i-1][j] + n)):
        ##print('hola')
        return True
  print('hola')    
  return False



#print(filasParecidasAanterior([[1],],3))   

print(filasParecidas([[1,2,3], [4,5,6]]))

# if __name__ == '__main__':
#   filas = int(input())
#   columnas = int(input())
 
#   matriz = []
 
#   for i in range(filas):         
#     fila = input()
#     if len(fila.split()) != columnas:
#       print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
#     matriz.append([int(j) for j in fila.split()])
  
#   print(filasParecidas(matriz))