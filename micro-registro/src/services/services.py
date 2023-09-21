
from modelos import candidato, prueba_tecnica, db


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
    new_test = prueba_tecnica(
        id_candidato=id_candidato,
        lenguaje =lenguaje,
        id_tipo_prueba = id_tipo_prueba,
        puntaje = puntaje,
        fecha = fecha,
        idioma = idioma,
        notas_evaluador = notas_evaluador
        )
    db.session.add(new_test)
    db.session.commit()
    return new_test