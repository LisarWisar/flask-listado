from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tareas(db.Model):
    __tablename__ = 'tareas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    prioridad = db.Column(db.Integer, nullable=False)
    estado= db.Column(db.String(30), nullable=False, default="Pendiente")

    def serialize(self):
        return {
        'id': self.id,
        'nombre': self.nombre,
        'prioridad': self.prioridad,
        'estado': self.estado,
        }