"""Módulo para realizar actividades relacionadas con la persistencia de datos.

Este módulo contiene funciones para realizar actividades de persistencia,
como guardar, leer y limpiar pedidos utilizando Flask y una conexión persistente
a una base de datos o archivos.

Las funciones y métodos aquí definidos interactúan con el módulo 'persistencia'
y utilizan las bibliotecas Flask para manejar solicitudes web y redirecciones.

Autor: José Manuel Carrasco López
Fecha de creación: 06/12/2023
"""
def guardar_pedido(nombre, apellidos, fichero):
    """Guarda un pedido en un archivo de texto.

    Esta función recibe el nombre y apellidos de un cliente y los guarda
    en un archivo de texto llamado 'pedidos.txt'.

    Args:
        nombre (str): El nombre del cliente.
        apellidos (str): Los apellidos del cliente.
        fichero (str): nombre del fichero donde se guardará la prueba

    Returns:
        None
    """
    with open(fichero, 'a', encoding='utf-8') as mi_fichero:
        mi_fichero.write("-" + nombre + " " + apellidos + "\n")
        mi_fichero.close()

def leer_pedidos(fichero):
    """Lee y muestra todos los pedidos guardados en el archivo 'pedidos.txt'.

    Args:
        fichero (str): nombre del fichero que se leerá

    Returns:
        None
    """
    with open(fichero, 'r', encoding='utf-8') as mi_fichero:
        for pedido in mi_fichero:
            print(pedido.strip())
        mi_fichero.close()

def limpiar_pedidos(fichero):
    """Limpia el contenido del archivo 'pedidos.txt'.

    Args:
        fichero (str): nombre del fichero al que se le borrará el contenido

    Returns:
        None
    """
    with open(fichero, 'w', encoding='utf-8') as mi_fichero:
        mi_fichero.write("")
        mi_fichero.close()


def leer_linea(fichero, numero_linea):
    """
    Devuelve la línea específica de un archivo dado su nombre y el número de línea.

    Args:
        fichero (str): El nombre del archivo del cual se desea obtener la línea.
        numero_linea (int): El número de línea que se quiere recuperar.

    Returns:
        str: La línea específica del archivo si se encuentra dentro del rango.
             Mensaje de advertencia si el número de línea está fuera del rango 
             del archivo o si ocurre un error.
    """
    try:
        with open(fichero, 'r', encoding='utf-8') as archivo:
            for num, linea in enumerate(archivo, start=1):
                if num == numero_linea:
                    return linea.rstrip('\n')  # Eliminar el salto de línea al final
            return f"El número de línea {numero_linea} está fuera del rango"
    except FileNotFoundError:
        return f"El archivo '{fichero}' no se encontró."
    except OSError as e:
        return f"Error al abrir o leer el archivo: {str(e)}"
