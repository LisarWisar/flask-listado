from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from blueprints.tareas import tareas_blueprint
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(tareas_blueprint, url_prefix="/tareas")
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
  app.run(host="localhost", port=5007, debug=True)

