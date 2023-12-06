def guardar_pedido(nombre, apellidos):
    """Guarda un pedido en un archivo de texto.

    Esta función recibe el nombre y apellidos de un cliente y los guarda
    en un archivo de texto llamado 'pedidos.txt'.

    Args:
        nombre (str): El nombre del cliente.
        apellidos (str): Los apellidos del cliente.

    Returns:
        None
    """    
    with open('pedidos.txt', 'a', encoding='utf-8') as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close()

def leer_pedidos():
    """Lee y muestra todos los pedidos guardados en el archivo 'pedidos.txt'.

    Lee el archivo 'pedidos.txt' línea por línea y muestra cada pedido en la consola.

    Returns:
        None
    """
    with open('pedidos.txt', 'r', encoding='utf-8') as file:
        for pedido in file:
            print(pedido.strip())
        file.close()

def limpiar_pedidos():
    """Limpia el contenido del archivo 'pedidos.txt'.

    Esta función borra todo el contenido del archivo 'pedidos.txt'.

    Returns:
        None
    """
    with open('pedidos.txt', 'w', encoding='utf-8') as file:
        file.write("")
        file.close()
