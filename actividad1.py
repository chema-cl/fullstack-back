"""Módulo para realizar actividades relacionadas con la persistencia de datos.

Este módulo contiene funciones para realizar actividades de persistencia,
como guardar, leer y limpiar pedidos utilizando Flask y una conexión persistente
a una base de datos o archivos.

Autor: José Manuel Carrasco López
Fecha de creación: 06/12/2023
"""
from flask import Flask, request, redirect
import persistencia

# URL Base, usaremos una constante por si en algún momento
# se publica en un sitio diferente a localhost
FRONT_END_URL_BASE  = "http://localhost/modulo1/actividad1"
FICHERO_PERSISTENCIA = "pedidos.txt"
app = Flask('Actividad-01')

@app.route('/pizza', methods=['POST'])
def procesar_pedido():
    """Procesa un pedido de pizza enviado mediante un formulario.

    Esta función se activa cuando se realiza una solicitud POST a '/pizza'.
    Obtiene los datos del formulario, como el nombre y apellidos del cliente,
    los imprime en la consola y guarda el pedido utilizando el módulo 'persistencia'.

    Returns:
        flask.redirect: Redirecciona a la página 'solicita_pedido.html' del frontend.
    """
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')

    # Imprimir los valores en la consola Python
    print("Nombre:", nombre)
    print("Apellidos:", apellidos)

    # Guardamos el pedido
    persistencia.guardar_pedido(nombre,apellidos,FICHERO_PERSISTENCIA)

    # Redireccionar a la página 'solicita_pedido.html'
    return redirect(FRONT_END_URL_BASE + "/solicita_pedido.html", code=302)

# Control para que solo se levante el servidor de escucha si usamos este fichero
# como principal y no si lo estamos imporatando desde otro
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
