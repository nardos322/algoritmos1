module Ej1 where

longitud:: [t] -> Integer
longitud [] = 0
longitud t = 1 + longitud (tail t)

ultimo:: [t] -> t
ultimo t    | longitud t == 1 = head t
            | otherwise = ultimo (tail t)

ultimo2:: [t] -> t
ultimo2(x:[]) = x
ultimo2(x:xs) = ultimo xs

principio:: [t] -> [t]
principio [x] = [x]
principio (x:xs) = x:(principio xs)

reverso:: [t] -> [t]
reverso s   | longitud s == 0 = []
            | otherwise = (ultimo s):reverso(principio s)

reverso2 [] = []
reverso2 s = (ultimo s):reverso2(principio s)

reverso3 [] = []
reverso3 (x:xs) = reverso3 xs ++ [x]
