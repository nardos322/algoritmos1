multiplosDeN':: Int -> [Int] -> [Int]
multiplosDeN' n [] = []
multiplosDeN' n (x:xs)  | esMultiplo x n = x : multiplosDeN' n xs
                        | not(esMultiplo x n) = multiplosDeN' n xs
