from http.client import NOT_FOUND
from flask import request
from flask_restful import Resource
from src.modelos import db, prueba_tecnica, candidato, candidatoSchema, SaveCandidate

prueba_tecnica_schema = prueba_tecnica()
candidato_schema = candidatoSchema(many=True)

class VistaConsultaPrueba(Resource):

    def get(self, id_prueba):
        return prueba_tecnica_schema.dump(prueba_tecnica_schema.query.get_or_404(id_prueba))
class VistaConsultaCandidato(Resource):

    def get(self):
        return candidato_schema.dump(candidato.query.all())
    
class VistaCrearCandidato(Resource):

    def post(self):
        data = request.json
        response = SaveCandidate(
            data['numid_nacional'],
            data['nombres'],
            data['apellidos'],
            data['telefono'],
            data['direccional'],
            data['edad'],
            data['ubicacion_geografica'],
            data['idiomas'],
            data['id_estado'],
            )
        return response