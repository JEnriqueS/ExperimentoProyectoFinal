from flask import Flask
# from flask_cors import CORS
from flask_restful import Api
from modelos import db
from vistas import (VistaConsultaPrueba, VistaConsultaCandidato, VistaCrearCandidato)
from dotenv import load_dotenv
import os
sqlpass = os.getenv("SQL_PASSWORD")
load_dotenv()

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI=''
if(os.path.isdir('/cloudsql/')):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'+sqlpass+'@/candidatos?unix_socket=/cloudsql/proyecto-final-01-399101:us-central1:candidatos'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'+sqlpass+'@34.71.192.222:3306/candidatos'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:'+sqlpass+'@34.71.192.222:3306/candidatos'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# cors = CORS(app)

api = Api(app)
# api.add_resource(VistaConsultaPrueba, '/prueba_tecnica/<int:id_prueba>')
api.add_resource(VistaConsultaCandidato, '/candidato/all')
api.add_resource(VistaCrearCandidato, '/candidato/insert')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)