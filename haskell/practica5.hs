import Practica4

pertenece:: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs) = n == x || pertenece n xs

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

eliminar::Int -> [Int] -> [Int]
eliminar n [] = []
eliminar n (x:xs)   | n == x = xs
                    | otherwise = x:(eliminar n xs)

descomponerEnPrimos:: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (descomponer x):(descomponerEnPrimos xs)

descomponer:: Integer -> [Integer]
descomponer n   | esPrimo n = [n] 
                | otherwise = (menorDivisor n):(descomponer(div n (menorDivisor n)))

