f :: Integer -> Integer
f x | x == 1 = 8
    | x == 4 = 131
    | x == 16 = 16


g :: Integer -> Integer 
g x | x == 8 =  16
    | x ==  16 = 4
    | x == 131 = 1

h :: Integer -> Integer
h x | x == 8 = f(g(x))
    | x == 16 = f(g(x))
    | x == 131 = f(g(x))

k :: Integer -> Integer
k x | x == 1 = g(f(x))
    | x == 4 = g(f(x))
    | x == 16 = g(f(x))    


y :: Int -> Int
y n = f(g(n))

z :: Int -> Int
z n = g(f(n))

