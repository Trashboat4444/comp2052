from flask import Blueprint, request, jsonify
from app.models import db, Articulo

# Blueprint solo con endpoints de prueba para articulos
main = Blueprint('main', __name__)

@main.route('/') # Ambas rutas llevan al mismo lugar
@main.route('/dashboard')
def index():
    """
    Página de inicio pública (home).
    """
    return '<h1>Corriendo en Modo de Prueba.</h1>'

@main.route('/articulos', methods=['GET'])
def listar_articulos():
    """
    Retorna una lista de articulos (JSON).
    """
    articulos = Articulo.query.all()

    data = [
        {'id': articulo.id, 'titulo': articulo.titulo, 'cuerpo': articulo.descripcion, 'profesor_id': articulo.profesor_id}
        for articulo in articulos
    ]
    return jsonify(data), 200


@main.route('/articulos/<int:id>', methods=['GET'])
def listar_un_articulo(id):
    """
    Retorna un solo articulo por su ID (JSON).
    """
    articulo = Articulo.query.get_or_404(id)

    data = {
        'id': articulo.id,
        'titulo': articulo.titulo,
        'descripcion': articulo.descripcion,
        'profesor_id': articulo.profesor_id
    }

    return jsonify(data), 200


@main.route('/articulos', methods=['POST'])
def crear_articulo():
    """
    Crea un articulo sin validación.
    Espera JSON con 'titulo', 'descripcion' y 'profesor_id'.
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    articulo = Articulo(
        titulo=data.get('titulo'),
        descripcion=data.get('cuerpo'),
        profesor_id=data.get('profesor_id')  # sin validación de usuario
    )

    db.session.add(articulo)
    db.session.commit()

    return jsonify({'message': 'Articulo creado', 'id': articulo.id, 'profesor_id': articulo.profesor_id}), 201

@main.route('/articulos/<int:id>', methods=['PUT'])
def actualizar_articulo(id):
    """
    Actualiza un articulo sin validación de usuario o permisos.
    """
    articulo = Articulo.query.get_or_404(id)
    data = request.get_json()

    articulo.titulo = data.get('titulo', articulo.titulo)
    articulo.descripcion = data.get('descripcion', articulo.descripcion)
    articulo.profesor_id = data.get('profesor_id', articulo.profesor_id)

    db.session.commit()

    return jsonify({'message': 'Articulo actualizado', 'id': articulo.id}), 200

@main.route('/articulos/<int:id>', methods=['DELETE'])
def eliminar_articulo(id):
    """
    Elimina un articulo sin validación de permisos.
    """
    articulo = Articulo.query.get_or_404(id)
    db.session.delete(articulo)
    db.session.commit()

    return jsonify({'message': 'Articulo eliminado', 'id': articulo.id}), 200
