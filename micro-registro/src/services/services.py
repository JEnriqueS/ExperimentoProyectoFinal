
from datetime import datetime
import random
from modelos import candidato, prueba_tecnica, db
from essential_generators import DocumentGenerator


def SaveCandidate(
        numid_nacional,
        nombres,
        apellidos,
        telefono,
        direccional,
        edad,
        ubicacion_geografica,
        idiomas,
        id_estado,
        ):
    new_Candidate = candidato(
        numid_nacional=numid_nacional,
        nombres =nombres,
        apellidos = apellidos,
        telefono = telefono,
        direccional = direccional,
        edad = edad,
        ubicacion_geografica = ubicacion_geografica,
        idiomas = idiomas,
        id_estado = id_estado
        )
    db.session.add(new_Candidate)
    db.session.commit()
    return new_Candidate

def SavePruebaTecnica(
        id_candidato,
        lenguaje,
        id_tipo_prueba,
        puntaje,
        fecha,
        idioma,
        notas_evaluador
        ):
    date_format = '%Y-%m-%d'
    dateObject = datetime.strptime(fecha, date_format)
    new_test = prueba_tecnica(
        id_candidato=id_candidato,
        lenguaje =lenguaje,
        id_tipo_prueba = id_tipo_prueba,
        puntaje = puntaje,
        fecha = dateObject,
        idioma = idioma,
        notas_evaluador = notas_evaluador
        )
    db.session.add(new_test)
    db.session.commit()
    return new_test

def GenerarPruebasTecnicas(cantidadPruebas, candidatedIds):
    lenguajes = ["Python", "C++", "C#", "GO", "Fortran","Cobol", "Java", "Javascript","PHP","R", "Swift", "Objective-C","Visual basic", "Perl"]
    tipos_prueba =[1,2]
    idiomas = ["Español", "Ingles", "Aleman", "Frances", "Portugues", "Italiano", "Mandarin", "Japones"]
    gen = DocumentGenerator()
    # notasEval = 


    for x in range(cantidadPruebas):
        id_candidato = random.choice(candidatedIds)
        lenguaje = random.choice(lenguajes)
        id_tipo_prueba = random.choice(tipos_prueba)
        puntaje = random.randint(1,100)
        mesRd = random.randint(1,12)
        diaRd = random.randint(1,30)
        if mesRd ==2 and diaRd>27:
            diaRd=27
        fecha = f'2023-{mesRd}-{diaRd}'
        idioma = random.choice(idiomas)
        notas_evaluador = gen.sentence()
        respTest = SavePruebaTecnica(
            id_candidato,
            lenguaje,
            id_tipo_prueba,
            puntaje,
            fecha,
            idioma,
            notas_evaluador
        )
        print("on: "+str(x))
    return "ok"