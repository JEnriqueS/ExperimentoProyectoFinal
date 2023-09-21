from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
class tipo_prueba(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

class estado_candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

class candidato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numid_nacional = db.Column(db.String(50))
    nombres = db.Column(db.String(100))
    apellidos = db.Column(db.String(100))
    telefono = db.Column(db.String(30))
    direccional = db.Column(db.String(200))
    edad = db.Column(db.SmallInteger)
    ubicacion_geografica = db.Column(db.String(200))
    idiomas = db.Column(db.String(200))
    id_estado = db.Column(db.Integer, db.ForeignKey('estado_candidato.id'))

class prueba_tecnica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidato.id'))
    lenguaje = db.Column(db.String(50))
    id_tipo_prueba = db.Column(db.Integer, db.ForeignKey('tipo_prueba.id'))
    puntaje = db.Column(db.Numeric, default=0)
    fecha = db.Column(db.DateTime)
    idioma = db.Column(db.String(20))
    notas_evaluador = db.Column(db.String(2000))



class tipo_pruebaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tipo_prueba
        include_relationships = True
        include_fk = True
        load_instance = True

class estado_candidatoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = estado_candidato
        include_relationships = True
        include_fk = True
        load_instance = True

class candidatoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = candidato
        include_relationships = True
        load_instance = True

class prueba_tecnicaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = prueba_tecnica
        include_relationships = True
        load_instance = True
    
    puntaje = fields.Float()

