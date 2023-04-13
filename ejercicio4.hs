{-HLINT ignore-}

prodInt :: (Float,Float) -> (Float, Float) -> Float
prodInt a b = (fst a * fst b) + (snd a * snd b)