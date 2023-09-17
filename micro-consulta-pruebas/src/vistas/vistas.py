from http.client import NOT_FOUND
from flask import request
from flask_restful import Resource
from src.modelos import db, prueba_tecnica, prueba_tecnicaSchema

prueba_tecnica_schema = prueba_tecnicaSchema()

class VistaConsultaPrueba(Resource):

    def get(self, id_prueba):
        return prueba_tecnica_schema.dump(prueba_tecnica.query.get_or_404(id_prueba))

class VistaConsultaTodasPruebas(Resource):

    def get(self):
        return [prueba_tecnica_schema.dump(prueba) for prueba in prueba_tecnica.query.all()]