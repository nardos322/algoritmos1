{-HLINT ignore-}
import Ejercicio2(esMultiploDe)

prodInt :: (Float,Float) -> (Float, Float) -> Float
prodInt a b = (fst a * fst b) + (snd a * snd b)


todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor a b   | fst a < fst b && snd a < snd b = True
                | otherwise = False

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos a b = sqrt((snd a - fst a)**2 + (snd b - fst b)**2)

sumaTerna :: (Int, Int, Int) -> Int
sumaTerna a = case a of (x,y,z) -> x + y + z

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x,y,z) n    | (esMultiploDe x n) && (esMultiploDe y n) && (esMultiploDe z n) = x + y + z
                                | (esMultiploDe x n) && (esMultiploDe y n) && not(esMultiploDe z n) = x + y
                                | (esMultiploDe x n) && not(esMultiploDe y n) && (esMultiploDe z n) = x + z
                                | not(esMultiploDe x n) && (esMultiploDe y n) && (esMultiploDe z n) =  y + z
                                | esMultiploDe x n = x
                                | esMultiploDe y n = y
                                | esMultiploDe z n = n
                                | otherwise = 0

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

invertir :: (a, b) -> (b, a)
invertir a = (snd a, fst a)