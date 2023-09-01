--import Ej1(longitud)
{-HLINT ignore-}

longitud:: [t] -> Integer
longitud [] = 0
longitud t = 1 + longitud (tail t)

pertenece:: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs)  | n == x = True
                    | otherwise = pertenece n (xs)

todosIguales:: (Eq t) => [t] -> Bool
todosIguales (x:xs) | x == head xs && longitud xs == 1 = True
                    | x == head xs = todosIguales xs
                    | otherwise = False

listaPerteneceLista:: (Eq t) => [t] -> [t] -> Bool
listaPerteneceLista [] ls = True

todosDistintos:: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs)   | pertenece x xs = False
                        | otherwise = todosDistintos xs

hayRepetidos:: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs

quitar:: (Eq t) => t -> [t] -> [t]
quitar n [] = []
quitar n (x:xs) | n /= x = x:quitar n xs
                | otherwise = xs                      

quitarTodos:: (Eq t) => t -> [t] -> [t]
quitarTodos n [] = []
quitarTodos n (x:xs)    | n /= x = x:quitarTodos n xs
                        | otherwise = quitarTodos n xs

eliminarRepetidos:: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x:eliminarRepetidos (quitar x xs)                