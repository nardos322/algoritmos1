import time
n = int(input('Numero a factorizar: '))



def esPrimo(n: int) -> bool:
    
    for i in range(2,n):
        if(n%i == 0):
            return False
        
    return True


def primo_numero(n: int) -> int:
    i: int = 2
    primos = []
    while i <= 100000000000000:
        
        if esPrimo(i):
            primos.append(i)
        i += 1
        if len(primos) == n:
            
            return primos[-1]       



def quitar_repetidos(l: list) -> list:
    sin_repetidos = []
    
    for i in l:
        
        if sin_repetidos.count(i) == 0:
            sin_repetidos.append(i)
    return sin_repetidos 
  
     
def factorizar_en_primos(n: int) -> list:
    factores_primos = []

    print('calculando..')
    
    time.sleep(0.5)
    for i in range(1,primo_numero(n)):
        
        while n%primo_numero(i)== 0:
                
                factores_primos.append(primo_numero(i))
                n = n/primo_numero(i)
                
        if n == 1:
            result = []
            
            bases = quitar_repetidos(factores_primos)
           
            for i in bases:
                base_expontente = (i,factores_primos.count(i))
                result.append(base_expontente)
                
            
            return result    
        
    
    
            

print(factorizar_en_primos(n))