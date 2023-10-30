from queue import LifoQueue 
from queue import Queue
from random import shuffle
import random




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



def palabra_mas_frecuente(nombre_archivo_input: str):
    archivo_input: str = open(nombre_archivo_input,'r')
    lista_palabras: list = []
    apariciones: list = []
    texto_formateado: list = []

    diccionario: dict = {}

    for line in archivo_input.readlines():
        
        lista_palabras += line.split()
    
    # este for me formatea las palabras que esan en lista_palabras, quita las mayusculas, '.' etc etc
    for word in lista_palabras:
        
        word = word.lower()
        word = word.replace('.','')
        word = word.replace(',','')
        texto_formateado.append(word)
        
    for word in texto_formateado:
        
        if word in diccionario:
            diccionario[word] += 1
        else:
            diccionario[word] = 1

    for i in diccionario.values():
        
        apariciones.append(i)
        

    for i in diccionario:
        if diccionario[i] == max(apariciones):
            return i   
  
    


def cantidad_de_apariciones(nombre_archivo_input: str, palabra: str) ->int:
    archivo_input: str = open(nombre_archivo_input,'r')
    lista_palabras: list = []
    texto_formateado: list = []
    contador: int = 0

    for line in archivo_input.readlines():
        lista_palabras += line.split()
    for word in lista_palabras:
        word = word.lower()
        word = word.replace('.','')
        word = word.replace(',','')
        word = word.replace('!','')
        texto_formateado.append(word)
    
  
    for word in texto_formateado:
        
        if word == palabra:
            contador += 1
    

    return contador        


def reverso(nombre_de_archivo_input: str) -> None:
    archivo_input: str = open(nombre_de_archivo_input, 'r')
    lista_palabras = []
    nombre_archivo_output: str = 'ejercicio_2_output.txt'
    archivo_output = open(nombre_archivo_output, 'w')

    for line in archivo_input.readlines():
        lista_palabras.append(line)

    for i in range(len(lista_palabras)-1,-1,-1):
        archivo_output.write(f"{lista_palabras[i]}\n")
    
    archivo_input.close()
    archivo_output.close()



def pertenece2(n: float, lista: list) -> bool:
    for numero in lista:
        
        if(numero == n):
            return True
        
    return False


def existe_palabra(palabra_input: str, nombre_archivo: str) -> bool:
    palabras_sin_tildes = []
    archivo_limpio: list = []
    text = ''
    archivo: str = open(nombre_archivo,'r')
    archivo = archivo.readlines()

    for linea in archivo:
        archivo_limpio.append(linea.replace('\n',''))

    for linea in archivo_limpio:
        text += linea

    text = text.replace('!',' ')    
    text = text.replace('¡','') 
    text = text.replace('/', ' ')   
    text = text.replace('(', '')
    text = text.replace(')','')
    text = text.replace(':',' ')
    text = text.replace('.',' ')
    text = text.replace('#', '')
    text = text.lower()
    separado_en_palabras = text.split()
    
    for palabra in separado_en_palabras:
        
        if(pertenece2('á',palabra) or pertenece2('é',palabra) or pertenece2('í',palabra) or pertenece2('ó',palabra) or pertenece2('ú',palabra)):
            
            if pertenece2('á',palabra):
                palabra_sin_tilde = palabra.replace('á', 'a')
                palabras_sin_tildes.append(palabra_sin_tilde)
            elif pertenece2('é',palabra):
                palabra_sin_tilde = palabra.replace('é','e')
                palabras_sin_tildes.append(palabra_sin_tilde)
            elif pertenece2('í',palabra):
                palabra_sin_tilde = palabra.replace('í','i')
                palabras_sin_tildes.append(palabra_sin_tilde)
            elif pertenece2('ó',palabra):
                palabra_sin_tilde = palabra.replace('ó','o')
                palabras_sin_tildes.append(palabra_sin_tilde)
            elif pertenece2('ú',palabra):
                palabra_sin_tilde = palabra.replace('ú','u')
                palabras_sin_tildes.append(palabra_sin_tilde)
           
        elif not(pertenece2('á',palabra) or pertenece2('é',palabra) or pertenece2('í',palabra) or pertenece2('ó',palabra) or pertenece2('ú',palabra)):
            
            palabras_sin_tildes.append(palabra)


    return pertenece2(palabra_input, palabras_sin_tildes) 



def contar_lineas(nombre_archivo: str) -> int:
    archivo_input: str = open(nombre_archivo, 'r')
    lineas: list = []

    for line in archivo_input.readlines():
        lineas.append(line)
    return len(lineas)    
    

def nueva_frase(name_file_input: str, phrase: str) -> str:
    file_input: str = open(name_file_input, 'r')
    new_phrase = []
   
    for line in file_input.readlines():
        
        new_phrase.append(line)
    
    new_phrase.append(phrase)
    file_input = open(name_file_input,'w')

    print(new_phrase)
    for line in new_phrase:
         file_input.write(line)
   
        
       
    


def nueva_frase_comienzo(name_file_input: str, phrase: str) -> str:
    file_input: str = open(name_file_input, 'r')
    new_phrase: list = [phrase]
    
    for line in file_input.readlines():
        new_phrase.append(line)
    file_input = open(name_file_input,'w')

    
    for line in new_phrase:
        if line == new_phrase[0]:
                file_input.write(f"{line}\n")
        else:

         file_input.write(line)
   


x = LifoQueue()

x.put(1)
x.put(2)
x.put(5)



def pila_copy(p: LifoQueue) -> LifoQueue:
    elements: list = []
    p_copy: LifoQueue = LifoQueue()
    while not p.empty():
        elements.append(p.get())
    for i in range(len(elements)-1,-1,-1):
            p.put(elements[i])
            p_copy.put(elements[i])
    return p_copy        
    

def cantidad_de_elementos(p: LifoQueue)-> int:
    p_copy: LifoQueue = pila_copy(p)
    contador: int = 0
    
    while not p_copy.empty():
        p_copy.get()
        contador += 1
    print(list(p.queue))
    return contador    


def generar_nros_al_azar(n: int, desde: int, hasta: int) -> LifoQueue:
    pila: LifoQueue = LifoQueue()

    for i in range(n):
        pila.put(random.randint(desde,hasta))
        
    print(list(pila.queue))
    return pila




def esta_bien_balanceada(s: str) -> bool:
    
    parentesis: list = []
    parentesis_de_apertura: list = []
    parentesis_de_cierre: list = []
    

    for i in s:
        if i == '(' or i == ')':
            parentesis.append(i)
    if  not (parentesis[0] == '('and len(parentesis)%2 == 0):
        return False
    for i in parentesis:
        if i == '(':
            parentesis_de_apertura.append(i)
        else:
            parentesis_de_cierre.append(i)    
    return len(parentesis_de_apertura) == len(parentesis_de_cierre)
    
    
              
       
def generar_nros_al_azar_colas(n: int, desde: int, hasta: int):
    cola: Queue = Queue()

    for i in range(n):
        cola.put(random.randint(desde, hasta))
    
    print(list(cola.queue))

    return cola    


c = Queue()
c.put((1,'n','c'))
c.put(43634)
c.put(4)
c.put(6)
c.put(25)



def cantidad_elementos_colas(c: Queue) -> int:
    elementos: list = []
    contador: int = 0

    while not c.empty():
        elementos.append(c.get())
        contador += 1
    
    
    # recontruccion de la cola
    for i in range(len(elementos)):
        c.put(elementos[i])
    
    return contador    


def buscar_el_maximo_colas(c: Queue) -> int:
    elementos: list = []

    while not c.empty():
        elementos.append(c.get())
    

    for i in range(len(elementos)):
        c.put(elementos[i])
    
    return max(elementos)    

pacientes = Queue()
pacientes.put((1,'n','cirujia'))
pacientes.put((6,'a','otorrino'))
pacientes.put((4,'x','dermatologo'))
pacientes.put((3,'y','oftalmologia'))
pacientes.put((3,'y','oftalmologia'))

def n_pacientes_urgentes(pacientes: Queue) -> int:
    lista_pacientes: list = []
    contador: int = 0
    

    while not pacientes.empty():
        lista_pacientes.append(pacientes.get())
      
    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][0] <= 3:
            contador += 1

    for i in range(len(lista_pacientes)):
        pacientes.put(lista_pacientes[i]) 

    print(list(pacientes.queue))        
    return contador


clientes_cola = Queue()
clientes_cola.put(('n',1, True, False))
clientes_cola.put(('e',9, False, False))
clientes_cola.put(('q',87, False, False))
clientes_cola.put(('hu',23, True, True))
clientes_cola.put(('j',7, True, False))
clientes_cola.put(('a',4, False, False))
clientes_cola.put(('x',2, True, True))

def a_clientes(clientes_cola: Queue) -> Queue:

    cola_de_atencion = Queue()
    lista_clientes: list = []
    clientes_con_prioridad: list = []
    clientes_con_cuenta: list = []
    clientes_sin_cuenta: list = []
    
    while not clientes_cola.empty():
        lista_clientes.append(clientes_cola.get())
    
    # aca los elementos de lista_clientes no estan ordenados por prioridad, separo en listas a los clientes con prioridad,
    #para despues ordenarlos 
    for i in range(len(lista_clientes)):
        
        if lista_clientes[i][3] == True:
            clientes_con_prioridad.append(lista_clientes[i])
            
        elif lista_clientes[i][2] == True:
            clientes_con_cuenta.append(lista_clientes[i]) 
             
        else:
            clientes_sin_cuenta.append(lista_clientes[i])

    #reescribo  lista_clientes con los clientes ahora ordenados por prioridad 
    #ejemplo a = [2,4,3,1], b=[1,2], c = [3,4] al hacer a = b + c las listas se concatenan
    # me quedaria a = [1,2,3,4]
    lista_clientes = clientes_con_prioridad + clientes_con_cuenta + clientes_sin_cuenta
    
    # como los elementos de lista_clientes ahora estan ordenados por prioridad agrego sus elementos
    # a cola_de_atencion
    for i in range(len(lista_clientes)):
        cola_de_atencion.put(lista_clientes[i])
    
    print(list(cola_de_atencion.queue))
    return cola_de_atencion


legajo = '2'

def promedio_estudiante(legajo: str) -> float:
    
    file_notas_alumnos: str = open('notas.csv', 'r')
    datos_alumnos = []
    notas_de_todos_alumnos = []
    notas_del_alumno = []
    for line in file_notas_alumnos.readlines():
            
            datos_alumnos.append(line)
    

    for notas in datos_alumnos:
        notas_de_todos_alumnos.append(notas.split(','))

    
    for i in range(len(notas_de_todos_alumnos)):
        
        if legajo == notas_de_todos_alumnos[i][0]:
            notas_del_alumno.append(notas_de_todos_alumnos[i][-1])
            

    print(notas_del_alumno)




promedio_estudiante('2')


