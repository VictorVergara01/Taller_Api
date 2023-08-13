from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos en memoria
db = []
id_counter = 1

# Crear (Create) un nuevo usuario


@app.route('/api/users', methods=['POST'])
def create_user():
    global id_counter
    data = request.json
    user = {'id': id_counter,
            'username': data['username'], 'email': data['email']}
    db.append(user)
    id_counter += 1
    return jsonify({'message': 'Usuario creado exitosamente', 'user': user}), 201

# Leer todos los usuarios (Read)


@app.route('/api/users', methods=['GET'])
def get_all_users():
    return jsonify(db)

# Leer un usuario específico por su ID (Read)


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in db if user['id'] == user_id), None)
    if user is None:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    return jsonify(user)

# Actualizar un usuario (Update)


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in db if user['id'] == user_id), None)
    if user is None:
        return jsonify({'message': 'Usuario no encontrado'}), 404
    data = request.json
    user['username'] = data['username']
    user['email'] = data['email']
    return jsonify({'message': 'Usuario actualizado exitosamente', 'user': user})

# Eliminar un usuario (Delete)


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global db
    db = [user for user in db if user['id'] != user_id]
    return jsonify({'message': 'Usuario eliminado exitosamente'})


if __name__ == '__main__':
    app.run(debug=True)
