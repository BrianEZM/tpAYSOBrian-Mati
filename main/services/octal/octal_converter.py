"""
Verifica si una cadena representa un número octal válido
Recibe un String ingresado por el usuario y verifica que solamente tenga los caracteres validos
"""


def es_octal(numero_str):
    if not numero_str:
        return False
    if numero_str[0] == '-':
        numero_str = numero_str[1:]
    return all(c in '01234567' for c in numero_str)


"""
Multiplica cada dígito octal por la potencia de 8 correspondiente 
a su posición (empezando desde la derecha con la 
potencia 0) y luego suma los resultados.
"""


def octal_a_decimal(octal_str):
    decimal = 0
    potencia = 0
    if octal_str.startswith('-'):
        es_negativo = True
        octal_str = octal_str[1:]
    else:
        es_negativo = False

    for digito in reversed(octal_str):
        decimal += int(digito) * (8 ** potencia)
        potencia += 1

    return -decimal if es_negativo else decimal


"""
Cada dígito octal se reemplaza por su equivalente de 3 bits en binario, 
concatenando los equivalentes
"""


def octal_a_binario(octal_str):
    # Diccionario con equivalencias
    tabla_octal_bin = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }
    binario = ""
    if octal_str.startswith('-'):
        es_negativo = True
        binario += '-'
        octal_str = octal_str[1:]

    # Concatenacion y asignacion: se accede al valor binario correspondiente al dígito octal iterado
    for digito in octal_str:
        binario += tabla_octal_bin[digito]

    # Eliminar ceros a la izquierda
    binario_sin_ceros_izquierda = binario.lstrip('0')

    # Manejar el caso del número 0
    if not binario_sin_ceros_izquierda:
        return "0"

    # Re-agregar el signo negativo si era necesario
    if es_negativo:
        return "-" + binario_sin_ceros_izquierda
    else:
        return binario_sin_ceros_izquierda


"""
Octal a Decimal: Multiplica cada dígito octal por la potencia de 8 
correspondiente a su posición (empezando desde la derecha con la potencia 0) y suma los resultados.

Decimal a Hexadecimal: Divide sucesivamente el número decimal por 16 y anota los restos en orden inverso. 
Los restos que sean mayores o iguales a 10 se reemplazan por 
sus equivalentes hexadecimales (A=10, B=11, C=12, D=13, E=14, F=15).
"""


def octal_a_hexadecimal(octal_str):
    decimal_val = octal_a_decimal(octal_str)
    if decimal_val == 0:
        return '0'

    # Variable donde se construira el valor
    hexadecimal = ''

    if decimal_val < 0:
        es_negativo = True
        decimal_val = -decimal_val
    else:
        es_negativo = False

    while decimal_val > 0:

        # Obtenemos el modulo, lo que "sobra", después de dividir por 16.
        residuo = decimal_val % 16
        condicion = residuo < 10
        if condicion:
            conversion_residuo = str(residuo)
            hexadecimal = conversion_residuo + hexadecimal
        else:
            valor_ascii_base = ord('A')
            ajuste = residuo - 10
            valor_ascii_hex = valor_ascii_base + ajuste
            caracter_hex = chr(valor_ascii_hex)
            hexadecimal = caracter_hex + hexadecimal

        # Se calcula el cociente de la división entera de decimal_val entre 16.
        # Este cociente se utilizará en la siguiente iteración del bucle para seguir dividiendo.
        cociente = decimal_val // 16
        decimal_val = cociente

    return '-' + hexadecimal.upper() if es_negativo else hexadecimal.upper()