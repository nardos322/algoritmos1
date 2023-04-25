import Ej1(longitud, ultimo)

pertenece:: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs)  | n == x = True
                    | otherwise = pertenece n (xs)

todosIguales:: (Eq t) => [t] -> Bool
todosIguales (x:xs) | x == head xs && longitud xs == 1 = True
                    | x == head xs = todosIguales xs
                    | otherwise = False
--quitar:: (Eq t) => t -> [t] ->[t]
--quitar e l  | head t == e  = tail l
--            | otherwise = (head l):(quitar e (tail l))

listaPerteneceLista:: (Eq t) => [t] -> [t] -> Bool
listaPerteneceLista [] ls = True


