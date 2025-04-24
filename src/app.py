from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, upgrade
from blueprints.tareas import tareas_blueprint
from models import db
import pymysql
import os
import time

app = Flask(__name__)

user = os.getenv("MYSQL_USER", "root")
password = os.getenv("MYSQL_PASSWORD:")
host = os.getenv("MYSQL_HOST", "mysql")
port = os.getenv("MYSQL_PORT", "3306")
database = os.getenv("MYSQL_DB")

def espera_inicio(retries=5, delay=5):
    user = os.getenv('MYSQL_USERNAME', "root")
    password = os.getenv('MYSQL_PASSWORD')
    host = os.getenv('MYSQL_HOST', "mysql")  
    port = os.getenv('MYSQL_PORT')
    database = os.getenv('MYSQL_DATABASE')
    for i in range(retries):
        try:
            conn = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                port=int(os.getenv('MYSQL_PORT', 3306)),
                connect_timeout=5
            )
            conn.close()
            return
        except pymysql.MySQLError:
            print(f"Esperando a que MySQL esté disponible... {i + 1}/{retries}")
            time.sleep(delay)
    raise RuntimeError("No se pudo conectar a MySQL después de varios intentos.")

espera_inicio()
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(tareas_blueprint, url_prefix="/tareas")
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)

