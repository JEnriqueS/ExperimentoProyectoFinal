from modelos import candidato, tipo_prueba

def test_new_tipo_prueba():
    candid = candidato()

    assert type(candid) == candidato

def test_new_tipo_prueba2():
    tipoPrueba = tipo_prueba()
    tipoPrueba.nombre='facilonga'

    assert tipoPrueba.nombre=='facilonga'

def test_new_tipo_prueba3():
    tipoPrueba = tipo_prueba()
    tipoPrueba.nombre='dificil'

    assert tipoPrueba.nombre=='dificiLLLLLL'