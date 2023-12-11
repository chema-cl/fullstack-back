"""
    Módulo prueba unitaria de calculadora
"""
import time
import calculadora

def test_sumar():
    """ Prueba unitaria método sumar"""
    time.sleep(1)
    a = 2
    b = 2
    c = calculadora.sumar(a, b)
    assert c == 4

def test_restar():
    """ Prueba unitaria método restar"""
    time.sleep(1)
    a = 2
    b = 2
    c = calculadora.restar(a, b)
    assert c == 0

def test_multiplicar():
    """ Prueba unitaria método multiplicar"""
    a = 2
    b = 3
    c = calculadora.multiplicar(a, b)
    assert c == 6
