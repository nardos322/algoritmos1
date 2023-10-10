
-- Ejercicio 1
votosEnBlanco :: [(String, String)] -> [Int] -> Int  -> Int
votosEnBlanco _ votosAfirmativos votosEfectuados = votosEfectuados - sumatoria votosAfirmativos


-- Ejercicio 2
formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True
formulasValidas ((" ",_):xs) = False
formulasValidas ((_," "):xs) = False
formulasValidas ((a,b):xs)  | pertenece (a,b) xs || pertenece (b,a) xs || estaEnOtraFormula (a,b) xs  = False
                            | otherwise = formulasValidas xs 


pertenece:: (Eq t) => t -> [t] -> Bool 
pertenece _ [] = False
pertenece n (x:xs)  | n == x = True
                    | otherwise = (pertenece n xs)

estaEnOtraFormula:: (String, String) -> [(String, String)] -> Bool
estaEnOtraFormula _ [] = False
estaEnOtraFormula (a,b) ((c,d):xs)  | a == c || a == d || b == c || b == d || a == b  = True
                                    | otherwise = (estaEnOtraFormula (a,b) xs)                  

-- Ejercicio 3
porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos presidente formulas votos = division (votosRecibidos presidente formulas votos) (sumatoria votos) 



division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b) 


sumatoria:: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

votosRecibidos:: String -> [(String, String)] -> [Int] ->  Int
votosRecibidos _ [(a,b)] [x] = x
votosRecibidos presidente ((a,b):formulas) (x:xs)   | presidente == a = x
                                                    | otherwise = votosRecibidos presidente formulas xs


-- Ejercicio 4
proximoPresidente :: [(String, String)] -> [Int] -> String
proximoPresidente [(presidente,vice)] _ = presidente
proximoPresidente ((presidente,vice):formulas) (x:xs)   | esMaximo x xs = presidente
                                                        | otherwise = proximoPresidente formulas xs

esMaximo:: Int -> [Int] -> Bool
esMaximo _ [] = True
esMaximo n (x:xs)   | n > x = esMaximo n xs
                    | otherwise = False