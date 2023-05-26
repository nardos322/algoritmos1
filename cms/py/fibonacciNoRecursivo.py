import sys

def fibonacciNoRecursivo(n: int) -> int:
  l: list = []

  for i in range(n+1):
    l.append(i)

  return esSecuenciaFibonacci(l)



def esSecuenciaFibonacci(l: list) -> int:
  l[0] = 0
  if(len(l) == 2):
    l[1] = 1
  
  for i in l:
    if(i >= 2):
      l[i] = l[i-1] + l[i-2]
  return l[i]




if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))