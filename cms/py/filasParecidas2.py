from typing import List

def filasParecidas2(matriz: List[List[int]]) -> bool :
  # Implementar esta funcion
  
   
  
  for i in range(len(matriz)):
      for j in range(len(matriz[0])):
          print(abs(matriz[i][j] - matriz[i-1][j]))
          
    


print(filasParecidas2([[1,2,3],[4,6,6]]))    
    