{-HLINT ignore -}

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b   | a `mod` b == 0 = True
                        | otherwise = False      