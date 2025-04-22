from flask import Blueprint, request, jsonify
from models import Tareas, db

tareas_blueprint = Blueprint("tareas", __name__)

@tareas_blueprint.route('/crear', methods=['POST'])
def agregar_tarea():
    try:
        data = request.get_json()
        data = {key.lower(): value for key, value in data.items()}
        tarea = data.get('tarea')
        prioridad = data.get('prioridad')
        if not tarea or not prioridad:
            return jsonify({'error': 'Los campos no pueden estar vacíos'}), 400
        try:
            prioridad = int(prioridad)
        except ValueError:
            return jsonify({'error': 'La prioridad debe ser un número entre 1 y 5'}), 400
        if not (1 <= prioridad <= 5):
            return jsonify({'error': 'La prioridad debe ser un número entre 1 y 5'}), 400
        lista = Tareas.query.filter(db.func.lower(Tareas.nombre) == tarea.lower()).first()
        if lista:
            return jsonify({'error': 'La tarea ya existe'}), 400
        nueva_tarea = Tareas(nombre=tarea, prioridad=prioridad)
        db.session.add(nueva_tarea)
        db.session.commit()
        return jsonify({'mensaje': 'Tarea agregada'}), 201
    except ValueError:
        return jsonify({'error': 'Ha ocurrido un error'}), 400
    except Exception as e:
        return jsonify({'error': "Ha ocurrido un error"}), 500
    
@tareas_blueprint.route('/', methods=['GET'])
def obtener_tareas():
    try:
        tareas = Tareas.query.order_by(Tareas.prioridad.desc()).all()
        if not tareas:
            return jsonify({"mensaje": "No hay tareas disponibles."}), 200
        tareas_id = [{"id": t.id, "tarea": t.nombre, "prioridad": t.prioridad, "estado": t.estado} for t in tareas]
        return jsonify(tareas_id), 200
    except:
        return jsonify({f"mensaje": "Ha ocurrido un error."}), 400
    
@tareas_blueprint.route('/completar/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    try:
        tarea = Tareas.query.get(id)
        if tarea:
            if tarea.estado == "Completado":
                return jsonify({"mensaje": "Esta tarea ya se encuentra completada."}), 200
            tarea.estado = "Completado"
            db.session.commit()
            return jsonify({'mensaje': 'Tarea Completada'}), 201
        return jsonify({'error': 'Tarea no encontrada'}), 404 
    except Exception as e: 
        return jsonify({'error': 'Ha ocurrido un error'}), 500

@tareas_blueprint.route('/eliminar/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    try:
        tarea = Tareas.query.get(id)
        if tarea:
            db.session.delete(tarea)
            db.session.commit()
            return jsonify({'mensaje': 'Tarea eliminada'}), 200
        return jsonify({'error': 'Tarea no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': 'Ha ocurrido un error'}), 500
