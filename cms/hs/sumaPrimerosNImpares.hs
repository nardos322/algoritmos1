--No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(sumaPrimerosNImpares(x ::(Integer)))
  }



sumaPrimerosNImpares :: Integer -> Integer
sumaPrimerosNImpares n = sumaAux(nEsimoImpar n)

sumaAux:: Integer -> Integer
sumaAux 0 = 1
sumaAux 1 = 4
sumaAux n = (2*n+2) + sumaAux(n-2)                    


sumaImpares:: Integer -> Integer
sumaImpares 0 = 0
sumaImpares n   | n < 0 = 0
                | n > 0 = nEsimoImpar n + sumaImpares(n-1)

nEsimoImpar:: Integer -> Integer
nEsimoImpar n = n*2-1