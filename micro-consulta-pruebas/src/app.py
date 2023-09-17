from flask import Flask
from flask_restful import Api
from src.modelos import db
from src.vistas import (VistaConsultaPrueba)
import os
sqlpass = os.getenv("SQL_PASSWORD")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:'+sqlpass+'@34.71.192.222:3306/candidatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaConsultaPrueba, '/prueba_tecnica/<int:id_prueba>')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)