from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from blueprints.tareas import tareas_blueprint
from models import db
import os

app = Flask(__name__)

# Old SQlite DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# New MySQL DB
user = os.getenv("MYSQL_USER", "root")
password = os.getenv("MYSQL_PASSWORD:")
host = os.getenv("MYSQL_HOST", "mysql")
port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DB")

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{user}:{password}@{host}:{port}/{database}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(tareas_blueprint, url_prefix="/tareas")
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)

