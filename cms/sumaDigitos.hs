-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(sumaDigitos(x ::(Int)))
  }

sumaDigitos :: Int -> Int
sumaDigitos n | n < 10 = n
              | otherwise = ultimo n + sumaDigitos(sacarUltimo n)

ultimo:: Int -> Int
ultimo a = a `mod` 10

sacarUltimo:: Int -> Int
sacarUltimo a = a `div` 10