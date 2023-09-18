module Practica4 where
{-Hlint ignore-}

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


esCapicua:: Integer -> Bool
esCapicua 0 = True
esCapicua n | cantDeDigitos n == 1 = True
            | iesimoDigito n 1 == resto n = esCapicua(sacarPrimero (sacarUltimo n))
            | otherwise = False


sacarPrimero:: Integer -> Integer
sacarPrimero n  | cantDeDigitos n > 1 = mod n (10^((cantDeDigitos n) - 1))
                | cantDeDigitos n == 1 = 0


menorDivisor:: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde:: Integer -> Integer -> Integer
menorDivisorDesde n k   | mod n k == 0 = k
                        | n == k = n
                        | otherwise = menorDivisorDesde n (k+1)


esPrimo:: Integer-> Bool
esPrimo n = menorDivisor n == n


sonCoprimos:: Integer -> Integer -> Bool
sonCoprimos _ 1 = True
sonCoprimos 1 _ = True
sonCoprimos a b | (a > b) && mod a (menorDivisor b) == 0 = False
                | (a > b) && mod a (menorDivisor b) /= 0 = sonCoprimos a (div b (menorDivisor b))
                | (b > a) && mod b (menorDivisor a) == 0 = False
                | (b > a) && mod b (menorDivisor a) /= 0 = sonCoprimos b (div a (menorDivisor a))

nEsimoPrimo:: Integer -> Integer
nEsimoPrimo n = (nEsimoPrimoHasta n 0 2)

nEsimoPrimoHasta:: Integer -> Integer -> Integer -> Integer
nEsimoPrimoHasta n i k  | n == i = k-1
                        | esPrimo k = (nEsimoPrimoHasta n (i+1) (k+1))
                        | not(esPrimo k) = (nEsimoPrimoHasta n i (k+1))
                        
                       
                        
                                