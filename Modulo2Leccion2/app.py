from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.config["SECRET_KEY"] = "mi_clave_secreta"

# Formulario de Registro
class RegisterForm(FlaskForm):
    username = StringField("Nombre de Usuario", validators=[DataRequired(), Length(min=3)])
    email = StringField("Correo", validators=[DataRequired(),Email()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Registrarse")

# Ruta del formulario
@app.route("/register", methods=["GET", "POST"])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        return f"Usuario registrado: {form.username.data} - {form.email.data}"
    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)