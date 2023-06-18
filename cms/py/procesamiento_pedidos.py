from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

pedidos = [
  {
    'id': 21,
    'cliente': 'Gabriela',
    'productos': {'manzana':2,'leche':4}
  },
  {
    'id': 1,
    'cliente': 'Juan',
    'productos': {'manzana': 2, 'pan': 4, 'factura': 6}
  }
 
]

stock_productos = {'manzana':10, 'leche':15, 'pan': 6, 'factura': 0}
precios_productos = {'manzana': 3.5, 'leche': 1.5, 'pan': 4, 'factura': 2.75}

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  
  cola_de_pedidos: Queue = Queue()
  for i in pedidos:
    cola_de_pedidos.put(i)

  # res = []

  
  pedido: dict = cola_de_pedidos.get()

  print(len(pedido['productos'].keys()))



procesamiento_pedidos(pedidos, stock_productos, precios_productos)



# if __name__ == '__main__':
#   pedidos: Queue = Queue()
#   list_pedidos = json.loads(input())
#   [pedidos.put(p) for p in list_pedidos]
#   stock_productos = json.loads(input())
#   precios_productos = json.loads(input())
#   print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}