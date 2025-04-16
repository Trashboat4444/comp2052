from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bienvenidos a mi API"

@app.route("/info", methods=["GET"])
def info():
    return "Esto es una Aplicacion Web con tres rutas"

@app.route("/crear_usuario",methods=["POST"])
def crear_usuario():
    data = request.get_json()
    if not data or 'nombre' not in data:
        return jsonify({"error": "falta el campo 'nombre' en el JSON"}), 400
    
@app.route("/usuarios",methods=["GET"])
def usuario():
    

if __name__ == "__main__":
    app.run(debug=True)