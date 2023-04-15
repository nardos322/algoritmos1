{-HLINT ignore -}
module Ejercicio2 where

    
absoluto :: Int -> Int
absoluto x  | x > 0 = x
            | otherwise = -x

maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y  | absoluto(x) > absoluto(y) = absoluto(x)
                    | otherwise = absoluto(y)


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

--mismoIntervalo :: Float -> Float -> Bool
--mismoIntervalo x y 

sumaDistintos :: (Num t, Eq t, Ord t) => t -> t -> t -> t
sumaDistintos a b c | a == b  = a + c
                    | a == c = a + b
                    | otherwise = a + b + c 


esMultiploDe :: Int -> Int -> Bool 
esMultiploDe a b    | a `mod` b == 0 = True
                    | otherwise = False                   


digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10

digitoDecenas :: Int -> Int 
digitoDecenas x = div (mod x 100) 10    

