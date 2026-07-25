"""Script super simple para probar GitHub Actions."""


def saludar(nombre):
    return f"Hola, {nombre}!"


def sumar(a, b):
    return a + b


if __name__ == '__main__':
    print(saludar('mundo'))
    print(f'2 + 3 = {sumar(2, 3)}')
