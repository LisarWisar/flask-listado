from flask import Flask, request, jsonify

app = Flask(__name__)
tareas = []


@app.route('/tareas/crear', methods=['POST'])
def agregar_tarea():
    data = request.get_json()
    tarea = data.get('tarea')
    prioridad = data.get('prioridad')
    if len(tareas) > 0:
        for t in tareas:
            if t['tarea'].lower() == tarea.lower():
                return jsonify({'error': 'La tarea ya existe'}), 400
    tareas.append({'tarea': tarea, 'prioridad': prioridad, "estado": "Pendiente"})
    tareas.sort(reverse=True, key=lambda x: x['prioridad'])
    return jsonify({'mensaje': 'Tarea agregada'}), 201

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    tareas_id = [{"id": i+1, "tarea": t["tarea"], "prioridad": t["prioridad"], "estado": t["estado"]} for i, t in enumerate(tareas)]
    return jsonify(tareas_id), 200

@app.route('/tareas/completar/<int:id>', methods=['put'])
def actualizar_tarea(id):
    if 0 < id <= len(tareas):
        if tareas[id-1]["estado"] == "Completado":
            return jsonify({"mensaje": "Esta tarea ya se encuentra completada."}), 200
        tareas[id-1]["estado"] = "Completado"
        return jsonify({'mensaje': 'Tarea Completada'}), 201
    elif len(tareas) == 0:
        return({"error": "El listado no tiene ninguna tarea."})
    return jsonify({'error': 'Tarea no encontrada'}), 404

@app.route('/tareas/eliminar/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    if 0 < id <= len(tareas):
        tareas.pop(id-1)
        return jsonify({'mensaje': 'Tarea eliminada'}), 200
    elif len(tareas) == 0:
        return({"error": "El listado no tiene ninguna tarea."})
    return jsonify({'error': 'Tarea no encontrada'}), 404

if __name__ == "__main__":
  app.run(host="localhost", port=5007, debug=True)

