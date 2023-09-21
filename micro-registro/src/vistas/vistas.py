from http.client import NOT_FOUND
from flask import request
from flask_restful import Resource
from modelos import db, prueba_tecnica, candidato, candidatoSchema
from services import SaveCandidate, SavePruebaTecnica

prueba_tecnica_schema = prueba_tecnica()
candidato_schema = candidatoSchema(many=True)
candidato_schema_single = candidatoSchema()

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
        return candidato_schema_single.dump(response)
class VistaCrearPrueba(Resource):

    def post(self):
        data = request.json
        response = SavePruebaTecnica(
            data['id_candidato'],
            data['lenguaje'],
            data['id_tipo_prueba'],
            data['puntaje'],
            data['fecha'],
            data['idioma'],
            data['notas_evaluador']
            )
        return candidato_schema_single.dump(response)