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

todosIguales:: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:y:xs)   | x == y = todosIguales(y:xs)
                        | otherwise = False

todosDistintos:: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs)   | pertenece x xs = False
                        | otherwise = todosDistintos xs


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

quitarTodos:: (Eq t) => t -> [t] -> [t]
quitarTodos n [] = []
quitarTodos n (x:xs)    | n == x = quitarTodos n (xs)
                        | otherwise = x:(quitarTodos n xs)

eliminarRepetidos:: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs)    | hayRepetidos (x:xs) = x:eliminarRepetidos(quitarTodos x xs)
                            | otherwise = (x:xs)

mismosElementos:: (Eq t) => [t] -> [t] -> Bool
mismosElementos a b = (mismosElementos' a b) && (mismosElementos' b a)


mismosElementos':: (Eq t) => [t] -> [t] -> Bool
mismosElementos' [] _ = True
mismosElementos' (x:xs) ys  | pertenece x ys = mismosElementos' xs ys
                            | otherwise = False



descomponerEnPrimos:: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (descomponer x):(descomponerEnPrimos xs)

descomponer:: Integer -> [Integer]
descomponer n   | esPrimo n = [n] 
                | otherwise = (menorDivisor n):(descomponer(div n (menorDivisor n)))

