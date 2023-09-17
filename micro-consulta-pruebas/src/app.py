from flask import Flask
# from flask_cors import CORS
from flask_restful import Api
from src.modelos import db
from src.vistas import (VistaConsultaPrueba, VistaConsultaCandidato, VistaCrearCandidato)
from dotenv import load_dotenv
import os
sqlpass = os.getenv("SQL_PASSWORD")
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:'+sqlpass+'@34.71.192.222:3306/candidatos'
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