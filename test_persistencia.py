"""
Test del módulo de persistencia

Autor: José Manuel Carrasco López
Fecha de creación: 06/12/2023
"""
import persistencia

FICHERO_PERSISTENCIA = "test_pedidos.txt"

def test_guardar_pedido():
    """
    Prueba la acción guardar pedidio del módulo de persistencia    
    """
    # vaciamos el fichero de pruebas de pedidos
    persistencia.limpiar_pedidos(FICHERO_PERSISTENCIA)

    # Guardamos el pedido
    persistencia.guardar_pedido("Juan","Gómez",FICHERO_PERSISTENCIA)
    persistencia.guardar_pedido("José","López",FICHERO_PERSISTENCIA)

    primera_linea = persistencia.leer_linea(FICHERO_PERSISTENCIA,1)
    segunda_linea = persistencia.leer_linea(FICHERO_PERSISTENCIA,2)

    assert primera_linea == "Juan Gómez"
    assert segunda_linea == "José López"
