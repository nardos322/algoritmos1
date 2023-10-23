from queue import LifoQueue 
from queue import Queue
from random import shuffle

def clonar_sin_comentarios(nombre_archivo_input: str) -> None:
    archivo_input = open(nombre_archivo_input, 'r')

    nombre_archivo_output: str = 'ejercicio_2_output.txt'
    archivo_output = open(nombre_archivo_output, 'w')

    for line in archivo_input.readlines():
        if not es_un_comentario(line):
            archivo_output.write(line)

    archivo_input.close()
    archivo_output.close()




def es_un_comentario(line: str) -> bool:

    for c in line:
        if c != ' ':
            if c == '#':
                return True
            return False
    return False


p: LifoQueue = LifoQueue()

p.put(2)
p.put(6)
p.put(7)

def buscar_el_maximo(p: LifoQueue) -> int:
    n: list[int] = []
    
    while not p.empty():

        n.append(p.get())
        
    for i in range(len(n)-1,0-1,-1):
        p.put(n[i])
        
    return max(n)






def armar_secuencia_de_bingo() -> Queue:
    x = range(0,100)
    numeros_random: list = []
    res: Queue = Queue()

    for i in x:
        numeros_random.append(i)

    shuffle(numeros_random)

    for i in numeros_random:
        res.put(i)
   

    return res
   

bolillero = armar_secuencia_de_bingo()   

def pertenece(l: list, n: int) -> bool:

    for i in range(len(l)):
        if l[i] == n:
            return True
        
    return False

def jugar_carton_de_bingo(carton: list, bolillero: Queue) -> int:
   
    
    jugadas = 0
    while not bolillero.empty():
        numero = bolillero.get()
           
        if pertenece(carton, numero):
            carton.remove(numero)
        else:
            jugadas += 1
        
        if len(carton) == 0:
            return jugadas


def agruparPorLongitud(nombre_de_archivo_input: str) -> dict:
    archivo_input = open(nombre_de_archivo_input,'r')

    res: dict = {}

    for line in archivo_input.readlines():
        for word in line.split():
            if len(word) not in res:
                res[len(word)] = 1
            else:
                res[len(word)] += 1
    archivo_input.close()
    
    return res            


print(jugar_carton_de_bingo([50], bolillero))
