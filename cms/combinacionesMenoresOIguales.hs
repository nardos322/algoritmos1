-- No editar esta parte
-- main :: IO()
-- main = do {
--   x <- readLn ;
--   print(combinacionesMenoresOiguales(x ::(Integer)))
--   }

-- combinacionesMenoresOiguales :: Integer -> Integer
-- combinacionesMenoresOiguales n = sumAux2(n)

combinacionesMenoresOIguales :: Integer -> Integer
combinacionesMenoresOIguales n = iterarI n n
  where
    iterarI :: Integer -> Integer -> Integer
    iterarI i n
      | i == 1 = iterarJ 1 n n
      | otherwise = iterarI (i - 1) n + iterarJ i n n
    iterarJ :: Integer -> Integer -> Integer -> Integer
    iterarJ i j n
      | j == 1 && i * j <= n = 1
      | j == 1 && i * j > n = 0
      | i * j <= n = iterarJ i (j - 1) n + 1
      | otherwise = iterarJ i (j - 1) n
