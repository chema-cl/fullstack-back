"""Módulo para realizar operaciones con una lista

Autor: José Manuel Carrasco López
Fecha de creación: 09/12/2023
"""
def obtener_primer_elemento(lista):
    """
    Función que devuelve el primer elemento de la lista pasada por parámetros
    Args:
      lista (list): lista de elementos
    Returns:
      Primer elemento de la lista
    """
    return lista[0]

def obtener_ultimo_elemento(lista):
    """
    Función que devuelve el último elemento de la lista pasada por parámetros
    Args:
      lista (list): lista de elementos
    Returns:
      Último elemento de la lista
    """
    return lista[len(lista) - 1]

def inserta_elemento_al_final(lista, elemento):
    """
    Función que añade un elemento al final de la lista
    Args:
      lista (list): lista de elementos
      elemento (str): elemento a añadir
    Returns:
      Lista con el elemento al final
    """
    lista.append(elemento)

def inserta_elemento_al_principio(lista, elemento):
    """
    Función que añade un elemento al principio de la lista
    Args:
      lista (list): lista de elementos
      elemento (str): elemento a añadir
    Returns:
      Lista con el elemento al principio
    """
    lista.insert(0, elemento)

def borra_lista(lista):
    """
    Función borra una lista
    Args:
      lista (list): lista de elementos
    Returns:
      NONE
    """
    lista.clear()
