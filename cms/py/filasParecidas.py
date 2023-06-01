from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
n_validas: List[bool] = []
def filasParecidas(matriz: List[List[int]]) -> bool :
  # Implementar esta funcion
  if(len(matriz) == 1):
     return True

  for n in range(-10000, 10000):
    
    res: bool = filasParecidasAanterior(matriz, n)
    if(len(res) == len(matriz[0])*(len(matriz)-1)):
      return True
    
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
      n_validas.append(n)
    else:
      n_validas.clear()
       
  return n_validas
  

    
    

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))