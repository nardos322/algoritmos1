{-HLINT ignore-}

f :: Integer -> Integer
f n | n <= 7 = n^2
    | n > 7 = 2*n - 1


g :: Int -> Int
g n | esPar n = div n 2
    | otherwise = 2*n + 1



esPar :: Int -> Bool
esPar n | n `mod` 2 == 0 = True
        | otherwise = False