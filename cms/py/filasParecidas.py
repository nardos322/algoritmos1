from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
solo_true: List[bool] = []
def filasParecidas(matriz: List[List[int]]) -> bool :
  # Implementar esta funcion
  for n in range(0, 4):
    res: bool = filasParecidasAanterior(matriz, n)
  return res
    # if(res == True):
    #   return res
   
  

def filasParecidasAanterior(matriz: List[List[int]], n: int):
  if(len(matriz) == 1):
     return True
  
  for i in range(1,len(matriz)):
    ##print('i',i)
    res = filaAnteriorMasN(matriz, i, n)
  return res

def filaAnteriorMasN(matriz: List[List[int]], i: int, n: int):
  

  for j in range(len(matriz[0])):
    
    #print('i', i,'j',j , 'n', n)
    if(matriz[i][j] == (matriz[i-1][j] + n)):
      solo_true.append(matriz[i][j] == (matriz[i-1][j] + n))
      ##print('i', i,'j',j , 'n', n, matriz[i][j] == (matriz[i-1][j] + n))
      ##print(solo_true)
  return solo_true

  



##print(filasParecidasAanterior([[1,2,3],[4,5,6]],1))   

print(filasParecidas([[1,2,3], [4,5,6],[7,8,20]]))

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