-- No editar esta parte
--main :: IO ()
--main = do
--  x <- readLn
--  print (sumaMenosQueMax (x :: (Int, Int, Int)))

--sumaMenosQueMax :: (Int, Int, Int) -> Bool
-- Completar acá la definición de la función

-- Pueden agregan las funciones que consideren necesarias

       

maximo:: Int -> Int -> Int -> Int
maximo a b c  | a >= b && a > c = a
              | b >= a && b > c = b
              | c >= a && c > b = c
              
minimo:: Int -> Int -> Int -> Int
minimo a b c  | a <= b && a < c = a
              | b <= a && b < c = b
              | c <= a && c < b = c

medio:: Int -> Int -> Int -> Int
medio a b c | (a < b && a > c) || (a > b && a < c) = a 
            | b > a && b < c || b < a && b > c = b
            | c < a && c > b || c > a && c < b = c
            
            