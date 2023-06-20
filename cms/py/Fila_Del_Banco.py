from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"



def avanzarFila(fila: Queue, min: int):
  #implementar función
  n = 0

  for i in range(min+1):
    
    if i%4 == 0:
      if i == 0:
        nueva_persona = fila.qsize()+1
        fila.put(nueva_persona)
        nueva_persona += 1
        
      if i > 0:
        fila.put(nueva_persona)
        nueva_persona += 1
      
    if i%10 == 1 and not fila.empty():
      
      fila.get()
      
    elif i%4 == 3 and not fila.empty():
      fila.get()
     
    if i%4 == 2 or (i%4 == 1 and i > 1):
      
      if i%4 == 2 and not fila.empty():
        n = fila.get()
        
      if i%4 == 1 and fila.empty():
        fila.put(n)



if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero) 
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

