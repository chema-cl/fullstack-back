def guardar_pedido(nombre, apellidos):
    with open('pedidos.txt', 'a', encoding='utf-8') as file:
        file.write(nombre + " " + apellidos + "\n")
        file.close()

def leer_pedidos():
    with open('pedidos.txt', 'r', encoding='utf-8') as file:
        for pedido in file:
            print(pedido.strip())
        file.close()

def limpiar_pedidos():
    with open('pedidos.txt', 'w', encoding='utf-8') as file:
        file.write("")
        file.close()    