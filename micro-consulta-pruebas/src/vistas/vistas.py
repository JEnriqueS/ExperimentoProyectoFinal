from http.client import NOT_FOUND
from flask import request
from flask_restful import Resource
from src.modelos import db, prueba_tecnica

prueba_tecnica_schema = prueba_tecnica()

class VistaConsultaPrueba(Resource):

    def get(self, id_prueba):
        return prueba_tecnica_schema.dump(prueba_tecnica_schema.query.get_or_404(id_prueba))