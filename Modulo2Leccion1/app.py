from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {"title": "Bienvenidos", "message": "¡Hola, Flask con Jinja2!"}
    return render_template('index.html', data=data)

@app.route('/usuarios')
def usuarios():
    lista_usuarios = ['Ana', 'Carlos', 'Beatriz', 'David']
    return render_template('usuarios.html', usuarios=lista_usuarios)

@app.route('/productos')
def productos():
    lista_productos = [
        {'nombre': 'Laptop', 'precio': 1200},
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Teclado', 'precio': 45}
    ]
    return render_template('productos.html', productos=lista_productos)

if __name__ == '__main__':
    app.run(debug=True)