-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(combinacionesMenoresOiguales(x ::(Integer)))
}

combinacionesMenoresOiguales :: Integer -> Integer
combinacionesMenoresOiguales n = sumaExterna n n n

sumaInterna:: Integer -> Integer -> Integer -> Integer
sumaInterna n _ 0 = 0
sumaInterna n i j | i*j <= n = 1 + sumaInterna n i (j-1)
                  | otherwise = sumaInterna n i (j-1)

sumaExterna:: Integer -> Integer -> Integer -> Integer
sumaExterna n 0 _ = 0
sumaExterna n i j = (sumaExterna n (i-1) j) + (sumaInterna n i j)



