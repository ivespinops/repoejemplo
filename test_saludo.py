from saludo import saludar, sumar


def test_saludar():
    assert saludar('Ivan') == 'Hola, Ivan!'


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
