{--HLINT ignore--}

absoluto :: Int -> Int
absoluto x  | x > 0 = x
            | otherwise = -x


maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y  | absoluto x > absoluto y = absoluto x
                    | otherwise = absoluto y


maximo3 :: Int -> Int -> Int -> Int
maximo3 a b c   | a > b && a > c = a
                | b > a && b > c = b
                | c > a && c > b = c


algunoEs0' :: Float -> Float -> Bool
algunoEs0' x y   | x == 0 || y == 0 = True
                 | otherwise = False


algunoEs0 :: Float -> Float -> Bool
algunoEs0 0 _ = True
algunoEs0 _ 0 = True
algunoEs0 _ _ = False

ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y   | x == 0 && y == 0 = True
                | otherwise = False

ambosSon0' :: Float -> Float -> Bool            
ambosSon0' 0 0 = True
ambosSon0' _ _ = False


mismoIntervalo:: Int -> Int -> Bool
mismoIntervalo a b  | a <= 3 && b <= 3 = True
                    | a > 3 && b <= 7 && b >= 3 = True
                    | a > 7 && b > 7 = True
                    | otherwise = False

sumaDistintos:: Int -> Int -> Int -> Int
sumaDistintos a b c | (a /= b) && (a /= c) && (b /= c) = a + b + c
                    | (a == b) && (a /= c) && (b /= c) = c
                    | (a /= b) && (a == c) && (b /= c) = b
                    | (a == b) && (a /= c) && (b == c) = a
                    | otherwise = 0

esMultiploDe:: Int -> Int -> Bool
esMultiploDe a b    | mod a b == 0 = True 
                    | otherwise = False

digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

digitoDecenas :: Int -> Int 
digitoDecenas x = div (mod x 100) 10


estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b   | a `mod` b == 0 = True
                        | otherwise = False

prodInt:: (Int, Int) -> (Int, Int) -> Int
prodInt a b = fst a * fst b + snd a * snd b

