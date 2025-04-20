from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    return f"Usuario: {username}, Contraseña: {password}"

if __name__ == "__main__":
    app.run(debug=True)