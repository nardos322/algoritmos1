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
    elements = []
    p_copy = LifoQueue()
    while not p.empty():
        elements.append(p.get())
    for i in range(len(elements)-1,-1,-1):
            p_copy.put(elements[i])
    return p_copy        
    

def cantidad_de_elementos(p: LifoQueue)-> int:
    
    contador = 0

    while not p.empty():
        elemento = p.get()
        contador += 1
    return contador    


#print(cantidad_de_elementos(x))
print(pila_copy(x))