multiplosDeN':: Int -> [Int] -> [Int]
multiplosDeN' n [] = []
multiplosDeN' n (x:xs)  | esMultiploDe x n = x : multiplosDeN' n xs
                        | not(esMultiploDe x n) = multiplosDeN' n xs
esMultiploDe :: Int -> Int -> Bool 
esMultiploDe a b    | a `mod` b == 0 = True
                    | otherwise = False                   
