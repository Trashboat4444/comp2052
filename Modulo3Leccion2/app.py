from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_changed, identity_loaded, AnonymousIdentity

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Requerido para manejo de sesiones

# --- Flask-Login Setup ---
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirige aqui cuando no se ha iniciado sesion

# --- Flask-Principal Setup ---
Principal(app)

# --- Clase de Usuario ---
class User(UserMixin):
    def __init__(self, id, role):
        self.id = id
        self.role = role

    def get_id(self):
        return self.id

# --- Usuarios de Ejemplo ---
users = {
    'admin': User('admin', 'admin'),
    'editor': User('editor', 'editor'),
    'user': User('user', 'user')
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# --- Permisos de Roles ---
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))
editor_permission = Permission(RoleNeed('editor'))

roles_permissions = {
    "admin": ["create", "read", "update", "delete"],
    "editor": ["read", "update"],
    "user": ["read"]
}

def check_permission(role, action):
    return action in roles_permissions.get(role, [])

# --- Identity Load Handler ---
@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    if current_user.is_authenticated:
        identity.provides.add(RoleNeed(current_user.role))

# --- Auth Routes ---
@app.route('/login/<role>')
def login(role):
    if role in users:
        user = users[role]
        login_user(user)
        identity_changed.send(app, identity=Identity(user.id))
        return f"Logged in as {role}"
    return "User not found", 404

@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    return "Logged out"

# --- Rutas Protegidas ---
@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin_panel():
    return "Welcome to the Admin Panel!"

@app.route('/edit')
@login_required
def edit():
    if check_permission(current_user.role, 'update'):
        return "Welcome to the Edit Page!"
    return "Access Denied", 403

@app.route('/view')
@login_required
def view():
    if check_permission(current_user.role, 'read'):
        return "Viewing content..."
    return "Access Denied", 403

# --- Ejecuta la aplicacion ---
if __name__ == "__main__":
    app.run(debug=True)
