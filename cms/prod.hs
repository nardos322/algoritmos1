-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(prod(x ::(Integer)))
  }
{-HLINT ignore-}

prod :: Integer -> Integer
prod 0 = 1
prod n = prodHasta(2*n)

prodHasta :: Integer -> Integer
prodHasta 0 = 1
prodHasta n = (n^2 + 2*n) * prodHasta(n - 1)

