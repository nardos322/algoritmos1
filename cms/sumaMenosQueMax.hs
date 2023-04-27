-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Int, Int, Int)))

sumaMenosQueMax :: (Int, Int, Int) -> Bool
sumaMenosQueMax (x,y,z) | maximo x y z > minimo x y z + medio x y z = True
                        | otherwise = False
                        
       

maximo:: Int -> Int -> Int -> Int
maximo 0 0 0 = 0
maximo a b c  | (a >= b) && (a >= c) = a
              | (b >= a) && (b >= c) = b
              | (c >= a) && (c >= b) = c
              
minimo:: Int -> Int -> Int -> Int
minimo 0 0 0 = 0
minimo a b c  | a <= b && a <= c = a
              | b <= a && b <= c = b
              | c <= a && c <= b = c

medio:: Int -> Int -> Int -> Int
medio 0 0 0 = 0
medio a b c | (a <= b && a >= c) || (a >= b && a <= c) = a 
            | b >= a && b < c || b <= a && b >= c = b
            | c <= a && c > b || c >= a && c <= b = c
            
            