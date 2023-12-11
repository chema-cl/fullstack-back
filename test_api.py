""" Test unitario del módulo api.py que maneja operaciones con listas

Autor: José Manuel Carrasco López
Fecha de creación: 09/12/2023
"""
import pytest
import api

# Definimos la lista base de nombres sobre la que vamos a trabajar
CONSTANTE_LISTA =  ["master", "full", "stack"]

def test_obtener_primer_elemento():
    """
    Test para probar función obtener primer elemento
    """
    lista = CONSTANTE_LISTA
    elemento = api.obtener_primer_elemento(lista)
    assert elemento == "master"

def test_inserta_elemento_al_final():
    """
    Test para probar función insertar al final
    """
    lista = CONSTANTE_LISTA
    api.inserta_elemento_al_final(lista, "hola")
    assert api.obtener_ultimo_elemento(lista) == "hola"

def test_inserta_elemento_al_principio():
    """
    Test para probar función insertar al principio
    """
    lista = CONSTANTE_LISTA
    api.inserta_elemento_al_principio(lista, "hola")
    assert api.obtener_primer_elemento(lista) == "hola"

def test_borra_lista():
    """
    Test para probar función borrar lista
    """
    lista = CONSTANTE_LISTA
    api.borra_lista(lista)
    assert len(lista) == 0
