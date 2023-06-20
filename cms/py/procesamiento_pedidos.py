from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json



# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  

  pedidos_procesados = []


 
  while not pedidos.empty():
  
    
    pedido_solicitado = pedidos.get()
    productos_solicitados = pedido_solicitado['productos'].keys()
    
    pedido_solicitado['precio_total']: float = 0  
    pedido_solicitado['estado']: str = '' 
    for producto in productos_solicitados:
      
      
      if stock_productos[producto] - pedido_solicitado['productos'][producto] >= 0:
       
        stock_productos[producto] -= pedido_solicitado['productos'][producto]
        
        pedido_solicitado['precio_total'] += pedido_solicitado['productos'][producto]*precios_productos[producto]
        
      else:
      
        pedido_solicitado['productos'][producto] = stock_productos[producto]
        stock_productos[producto] -= stock_productos[producto]
        pedido_solicitado['precio_total'] += pedido_solicitado['productos'][producto]*precios_productos[producto]
        pedido_solicitado['estado'] = 'incompleto' 
      if  not pedido_solicitado['estado'] == 'incompleto':
        pedido_solicitado['estado'] = 'completo'
    pedidos_procesados.append(pedido_solicitado)    
    
  return pedidos_procesados    
 




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