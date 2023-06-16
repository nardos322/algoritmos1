{-HLINT ignore-}

sumaUltimosDosDigitos:: Integer -> Integer
sumaUltimosDosDigitos x = (x `mod` 10) + (x `div` 10) `mod` 10

comparar:: Integer -> Integer -> Integer
comparar a b    | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
                | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = -1
                | sumaUltimosDosDigitos(a) == sumaUltimosDosDigitos(b) = 0


-- listaLlegadas ejercicio que tomaron en el parcial 15/06/23

listaLlegadas:: [(Char,Char)] -> [Char] -> [Char]
listaLlegadas _ [] = []
listaLlegadas listaDeVuelos (partida:partidas)  | llegadaDeCadaVuelo listaDeVuelos partida ==  ' ' = listaLlegadas listaDeVuelos partidas
                                                | otherwise = llegadaDeCadaVuelo listaDeVuelos partida:listaLlegadas listaDeVuelos partidas

llegadaDeCadaVuelo:: [(Char,Char)] -> Char -> Char
llegadaDeCadaVuelo [] _ = ' '
llegadaDeCadaVuelo (vuelo:vuelos) partida   | fst vuelo == partida = snd vuelo
                                            | otherwise = llegadaDeCadaVuelo vuelos partida

