{-HLINT ignore-}

sumaUltimosDosDigitos:: Integer -> Integer
sumaUltimosDosDigitos x = (x `mod` 10) + (x `div` 10) `mod` 10

comparar:: Integer -> Integer -> Integer
comparar a b    | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
                | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = -1
                | sumaUltimosDosDigitos(a) == sumaUltimosDosDigitos(b) = 0