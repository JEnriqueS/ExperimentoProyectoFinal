
from modelos import candidato, db


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