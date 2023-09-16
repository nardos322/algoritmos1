import Practica4
{-Hlint ignore-}

longitud:: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo:: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

principio:: [t] -> [t]
principio [x] = []
principio (x:xs) = x:principio(xs)

pertenece:: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs) = n == x || pertenece n xs

reverso::(Eq t) => [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = ultimo(xs):reverso(eliminar(ultimo xs) (x:xs))

hayRepetidos:: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) =  pertenece x xs || hayRepetidos xs

maximo::[Int] -> Int
maximo [x] = x
maximo (x:y:ys) | x >= y = maximo(x:ys)
                | otherwise = maximo(y:ys)


ordenar::[Int] -> [Int]
ordenar [] = []
ordenar (x:xs) = ordenar(eliminar max (x:xs))++[max]
                where max = maximo(x:xs)

eliminar::(Eq t) => t -> [t] -> [t]
eliminar n [] = []
eliminar n (x:xs)   | n == x = xs
                    | otherwise = x:(eliminar n xs)

descomponerEnPrimos:: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (descomponer x):(descomponerEnPrimos xs)

descomponer:: Integer -> [Integer]
descomponer n   | esPrimo n = [n] 
                | otherwise = (menorDivisor n):(descomponer(div n (menorDivisor n)))

