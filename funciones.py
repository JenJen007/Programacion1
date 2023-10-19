#funcion para sumar digitos
def sumatoria(x):
    add = 0
    while x != 0:
        digit = x%10
        x //= 10
        add += digit
    return add


