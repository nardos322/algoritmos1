import sys
from queue import Queue
sys.path.append('../')
from procesamiento_pedidos import procesamiento_pedidos

print(sys.path)


def test_procesamiento_pedidos():

    pedidos_en_cola = Queue()
    
    pedidos = [
        {
            'id': 21,
            'cliente': 'Gabriela',
            'productos': {'manzana':2}
        },
        {
            'id': 1,
            'cliente': 'Juan',
            'productos': {'manzana': 2, 'pan': 7, 'factura': 6}
        },
        {
            'id': 4,
            'cliente': 'Lorenzo',
            'productos': {'manzana': 4, 'pan': 2, 'factura': 2}
        }
 
    ]


    for i in pedidos:
        pedidos_en_cola.put(i)

    stock_productos = {'manzana':3, 'pan': 0, 'factura':20}
    precios_productos = {'manzana': 1, 'pan': 0, 'factura': 2}

    assert procesamiento_pedidos(pedidos_en_cola, stock_productos, precios_productos) == [
        {   
            'id': 21, 
            'cliente': 'Gabriela',
            'productos': {'manzana': 2},
            'precio_total': 2, 
            'estado': 'completo'
        }, 
        {
            'id': 1, 
            'cliente': 'Juan', 
            'productos': {'manzana': 1, 'pan': 0, 'factura': 6}, 
            'precio_total': 13, 'estado': 'incompleto'}, 
        {
            'id': 4, 
            'cliente': 'Lorenzo', 
            'productos': {'manzana': 0, 'pan': 0, 'factura': 2}, 
            'precio_total': 4, 
            'estado': 'incompleto'
        }
    ]




def test_procesamiento_pedidos2():
    
    pedidos_en_cola2 = Queue()
    
    pedidos2 = [
        {
            'id': 21,
            'cliente': 'Gabriela',
            'productos': {'manzana':2}
        },
        { 
            'id': 1,
            'cliente': 'Juan',
            'productos': {'manzana': 2, 'pan': 7, 'factura': 6}
        },
        {
            'id': 4,
            'cliente': 'Lorenzo',
            'productos': {'manzana': 4, 'pan': 2, 'factura': 2}
        }
 
    ]

    for i in pedidos2:
        pedidos_en_cola2.put(i)

    stock_productos2 = {'manzana':0, 'pan': 0, 'factura':0}
    precios_productos2 = {'manzana': 1, 'pan': 0, 'factura': 2}        
    
    
    assert procesamiento_pedidos(pedidos_en_cola2, stock_productos2, precios_productos2) == [
        {   
            'id': 21, 
            'cliente': 'Gabriela',
            'productos': {'manzana': 0},
            'precio_total': 0, 
            'estado': 'incompleto'
        }, 
        {
            'id': 1, 
            'cliente': 'Juan', 
            'productos': {'manzana': 0, 'pan': 0, 'factura': 0}, 
            'precio_total': 0, 
            'estado': 'incompleto'}, 
        {
            'id': 4, 
            'cliente': 'Lorenzo', 
            'productos': {'manzana': 0, 'pan': 0, 'factura': 0}, 
            'precio_total': 0, 
            'estado': 'incompleto'
        }
    ]