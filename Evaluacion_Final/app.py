from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Función que devuelve el total con descuento aplicado
def descuento_pintura(edad, total_pintura):
    if 18 <= edad <= 30:
        return total_pintura * 0.85   # 15% de descuento
    elif edad > 30:
        return total_pintura * 0.75   # 25% de descuento
    else:
        return total_pintura          # sin descuento

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    datos = None

    if request.method == 'POST':
        nombre = request.form['Nombre']
        edad = int(request.form['Edad'])
        pintura = int(request.form['Pintura'])

        total_sin = pintura * 9000  # precio unitario ejemplo
        total_final = descuento_pintura(edad, total_sin)
        descuento = total_sin - total_final

        datos = {
            "nombre": nombre,
            "total_sin": total_sin,
            "descuento": descuento,
            "total_final": total_final
        }

    return render_template('ejercicio1.html', datos=datos)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    # Usuarios registrados
    usuarios = {
        "juan": "admin",
        "pepe": "user"
    }

    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']

        if usuario in usuarios and clave == usuarios[usuario]:
            if usuario == "juan":
                mensaje = f"Bienvenido administrador {usuario}"
            elif usuario == "pepe":
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run()