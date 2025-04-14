from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bienvenidos a mi API"

@app.route("/info", methods=["GET"])
def info():
    return "Esto es una Aplicacion Web con dos rutas"

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json
    nombre = data.get("nombre", "Usuario")
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    app.run(debug=True)