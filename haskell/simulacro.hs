{-Hlint ignore-}

relacionesValidas:: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:xs)  | incluido [x] (xs) || incluidoTuplas x xs || fst x == snd x = False
                          | otherwise = relacionesValidas xs

personas:: [(String,String)] -> [String]
personas [] = []
personas ((persona1,persona2):relaciones) = persona1:persona2:(personas relaciones)



incluidoTuplas:: (String,String) -> [(String,String)] -> Bool
incluidoTuplas _ [] = False
incluidoTuplas (a,b) ((c,d):xs)     | (a == c && b == d) || (a == d && b == c) = True
                                    | otherwise = incluidoTuplas (a,b) xs


amigosDe:: String -> [(String,String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((a,b):xs) | persona == a = b:amigosDe persona xs
                            | persona == b = a:amigosDe persona xs
                            | otherwise = amigosDe persona xs


personasConRepetidos:: [(String,String)] -> [String]
personasConRepetidos [] = []
personasConRepetidos ((a,b):xs) = a:b:(personasConRepetidos xs)


sacarRepetidos:: [String] -> [String]
sacarRepetidos [] = []
sacarRepetidos (x:xs)   | pertenece x xs = sacarRepetidos xs
                        | otherwise = (x:sacarRepetidos xs)
personas':: [(String,String)] -> [String]
personas' xs = sacarRepetidos(personasConRepetidos xs)



pertenece:: (Eq t) => t -> [t] -> Bool
pertenece n [] = False
pertenece n (x:xs) = n == x || pertenece n xs


quitar :: (Eq t) => t -> [t] -> [t]
-- requiere x pertenece a y
quitar x (y:ys) | x == y = ys
                | otherwise = y : quitar x ys 

longitud:: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs


incluido :: (Eq t) => [t] -> [t] -> Bool
incluido [] l = True
incluido (x:c) l = elem x l && incluido c (quitar x l)

sonIguales :: (Eq t) => [t] -> [t] -> Bool
sonIguales xs ys = incluido xs ys && incluido ys xs 

personaConMasAmigos:: [(String,String)] -> String
personaConMasAmigos xs = personaConMasAmigosAux (personas xs) xs

cantDeAmigos:: String -> [(String,String)] -> Integer
cantDeAmigos p rel = longitud(amigosDe p rel)


personaConMasAmigosAux:: [String] -> [(String,String)] -> String
personaConMasAmigosAux [x] _ = x 
personaConMasAmigosAux (x:y:xs) relaciones  | cantDeAmigos x relaciones > cantDeAmigos y relaciones = personaConMasAmigosAux(x:xs) relaciones
                                            | otherwise = personaConMasAmigosAux(y:xs) relaciones