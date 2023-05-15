import Ejercicio2(esMultiploDe)
{-Hlint ignorre-}

bisiesto :: Int -> Bool
bisiesto n  | (not(esMultiploDe n 4)) || (esMultiploDe n 100 && not (esMultiploDe n 400)) = False
            | otherwise = True