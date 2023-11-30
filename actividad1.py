import persistencia
from flask import Flask, request, redirect

#URL Base, usaremos una constante por si en algún momento se publica en un sitio diferente a localhost
frontEndURLBase = "http://localhost/modulo1/actividad1"
app = Flask('Actividad-01')

@app.route('/pizza', methods=['POST'])
def procesar_pedido():
    # Obtener los datos del formulario
    nombre = request.form.get('nombre')
    apellidos = request.form.get('apellidos')

    # Imprimir los valores en la consola Python
    print("Nombre:", nombre)
    print("Apellidos:", apellidos)

    # Guardamos el pedido
    persistencia.guardar_pedido(nombre,apellidos)   

    # Redireccionar a la página 'solicita_pedido.html'
    return redirect(frontEndURLBase + "/solicita_pedido.html", code=302)

# Control para que solo se levante el servidor de escucha si usamos este fichero 
# como principal y no si lo estamos imporatando desde otro
if __name__ == '__main__':
    app.run(host='localhost', port=5000)