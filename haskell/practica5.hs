--import Practica4--


menorDivisor:: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde:: Integer -> Integer -> Integer
menorDivisorDesde n k   | mod n k == 0 = k
                        | n == k = n
                        | otherwise = menorDivisorDesde n (k+1)


esPrimo:: Integer-> Bool
esPrimo n = menorDivisor n == n

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
reverso (x:xs) = reverso xs ++ [x]

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

capicua:: (Eq t) => [t] -> Bool
capicua xs = xs == reverso(xs)

descomponerEnPrimos:: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = (descomponer x):(descomponerEnPrimos xs)

descomponer:: Integer -> [Integer]
descomponer n   | esPrimo n = [n] 
                | otherwise = (menorDivisor n):(descomponer(div n (menorDivisor n)))

sumatoria:: (Num t) => [t] -> t
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

productoria:: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x*productoria xs

sumarN:: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = n+x:(sumarN n xs)


sumarElPrimero:: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo:: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo(x:xs)) (x:xs)

pares::[Integer] -> [Integer]
pares [] = []
pares (x:xs)    | mod x 2 == 0 = x:pares xs 
                | otherwise = pares xs

multiplosDeN:: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs)   | mod x n == 0 = x:multiplosDeN n xs
                        | otherwise = multiplosDeN n xs


sacarBlancosRepetidos:: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:xs)  | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:xs)
                                | otherwise = x:sacarBlancosRepetidos (y:xs)

contarPalabras:: [Char] -> Integer
contarPalabras (x:xs) = contarEspacios(sacarEspacioInicioFin(sacarBlancosRepetidos (x:xs))) + 1
                       

contarEspacios:: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs)   | x == ' ' = 1 + contarEspacios(xs)
                        | otherwise = contarEspacios(xs)                         

sacarEspacioInicio:: [Char] -> [Char]
sacarEspacioInicio [] = []
sacarEspacioInicio (x:xs)   | x == ' ' = sacarEspacioInicio (sacarBlancosRepetidos xs)
                            | otherwise = sacarBlancosRepetidos (x:xs)

sacarEspacioInicioFin:: [Char] -> [Char]
sacarEspacioInicioFin [] = []
sacarEspacioInicioFin (x:xs)    | ultimo (x:xs) == ' ' = sacarEspacioInicioFin(principio (x:xs))
                                | otherwise = sacarEspacioInicio(x:xs)


palabras:: [Char] -> [[Char]]
palabras [] = []
palabras (x:xs) = primeraPalabra(sacarEspacioInicio(x:xs)):palabras(sacarPrimeraPalabra(sacarEspacioInicio(x:xs)))


primeraPalabra:: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs)   | x == ' ' = []
                        | otherwise = x:(primeraPalabra xs)

sacarPrimeraPalabra:: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs)  | x == ' ' =  sacarEspacioInicioFin xs
                            | otherwise = sacarPrimeraPalabra xs


palabraMasLarga:: [Char] -> [Char]
palabraMasLarga (x:xs) = palabraMasLargaAux(palabras((x:xs)))

palabraMasLargaAux:: [[Char]] -> [Char]
palabraMasLargaAux [x] = x
palabraMasLargaAux (xs:xy:xss)  | longitud(sacarEspacioInicioFin(xs)) >= longitud(sacarEspacioInicioFin(xy))  = palabraMasLargaAux(xs:xss)
                                | otherwise = palabraMasLargaAux(xy:xss)

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (xs:xss) = xs ++ (aplanar xss)

aplanarConBlancos:: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (xs:xss) = xs ++ [' '] ++  sacarEspacioInicioFin(aplanarConBlancos(xss))

aplanarConNBlancos:: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] n = []
aplanarConNBlancos (xs:xss) n   | n /= 0 = xs ++ [' '] ++  sacarEspacioInicioFin(aplanarConNBlancos xss (n-1))
                                | otherwise = xs ++ sacarEspacioInicioFin(aplanarConNBlancos xss n)


sumaAcumulada:: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada (x:xs) =  (x:xs)



numeroSiguiente:: (Num t) => [t] -> t
numeroSiguiente [x] = x 
numeroSiguiente (x:y:xs) = y