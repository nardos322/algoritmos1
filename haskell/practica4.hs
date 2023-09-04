
sumatoriaInterna:: Integer -> Integer -> Integer
sumatoriaInterna _ 0 = 0
sumatoriaInterna n j = n^j + sumatoriaInterna n (j-1)

sumatoriaDoble:: Integer -> Integer -> Integer
sumatoriaDoble 0 _ = 0
sumatoriaDoble n m = sumatoriaDoble (n-1) m + sumatoriaInterna n m

fibonacci:: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)


parteEntera:: Float -> Integer
parteEntera x | x < 1 = 0
parteEntera x | otherwise =  1 + parteEntera(x-1)

esDivisible:: Integer -> Integer -> Bool
esDivisible _ 1 = True  
esDivisible 0 _ = True
esDivisible _ 0 = False
esDivisible a b | b > a = False 
esDivisible a b | a < 0 = False
esDivisible a b | otherwise = esDivisible(a-b) b


sumaImpares:: Integer -> Integer
sumaImpares 0 = 0
sumaImpares 1 = 1
sumaImpares n = 2*n-1 + sumaImpares(n-1) 

sumaImpares' :: Integer -> Integer
sumaImpares' n = n^2


medioFact:: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact n = n*medioFact(n-2)


sumaDigitos:: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = resto(n) + sumaDigitos(sacarUltimo(n))

resto:: Integer -> Integer
resto n = mod n 10

sacarUltimo:: Integer -> Integer
sacarUltimo n = div n 10


todosDigitosIguales:: Integer -> Bool
todosDigitosIguales n = resto(n) == resto(sacarUltimo(n))


cantDeDigitos:: Integer -> Integer
cantDeDigitos 0 = 0
cantDeDigitos n = 1 + cantDeDigitos(sacarUltimo(n))

iesimoDigito:: Integer -> Integer -> Integer
iesimoDigito n i = n `div` 10^(cantDeDigitos(n)-i) `mod` 10

