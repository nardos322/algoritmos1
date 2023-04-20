{-HLINT ignore-}

fibonacci:: Integer -> Integer
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)


parteEntera:: Float -> Integer
parteEntera n   | n < 1 = 0
                | n > 1 = 1 + parteEntera(n-1)

esDivisible:: Integer -> Integer -> Bool
esDivisible _ 0 = False
esDivisible _ 1 = True
esDivisible 0 _ = True
esDivisible a b | a - b < 0 = False
                | a - b == 0 = True
                | otherwise = esDivisible(a-b) b


sumaImpares:: Integer -> Integer
sumaImpares 0 = 0
sumaImpares n   | n < 0 = 0
                | n > 0 = nEsimoImpar n + sumaImpares(n-1)

nEsimoImpar:: Integer -> Integer
nEsimoImpar n = n*2-1
                      