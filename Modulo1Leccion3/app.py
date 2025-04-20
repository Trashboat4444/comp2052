from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista para almacenar usuarios en memoria
usuarios = []

@app.route("/", methods=["GET"])
def home():
    return "Bienvenidos a mi API"

@app.route("/info", methods=["GET"])
def info():
    return "Esto es una Aplicacion Web con tres rutas"


@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.json
    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:
        return jsonify({"error": "Nombre y correo son obligatorios"}), 400

    nuevo_usuario = {"nombre": nombre, "correo": correo}
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado con éxito", "usuario": nuevo_usuario}), 201

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)