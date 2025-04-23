# Verifica si una cadena representa un número octal válido
def es_decimal(numero_str):
    if not numero_str:
        return False
    if numero_str[0] == '-':
        numero_str = numero_str[1:]
    return all(c in '0123456789' for c in numero_str)


def decimal_a_binario(numero):
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario


def decimal_a_octal(numero):
    octal = ""
    while numero > 0:
        residuo = numero % 8
        octal = str(residuo) + octal
        numero = int(numero / 8)
    return octal


def obt_caracter(valor):
    valor = str(valor)
    equivalencias = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor


def decimal_a_hexadecimal(numero):
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        caracter = obt_caracter(residuo)
        hexadecimal = caracter + hexadecimal
        numero = int(numero / 16)
    return hexadecimal
