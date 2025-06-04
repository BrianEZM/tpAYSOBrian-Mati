"""
Verifica si una cadena representa un número binario válido
Recibe un String ingresado por el usuario y verifica que solamente tenga los caracteres validos (0 y 1)
"""


def es_binario(numero_str):
    if not numero_str:
        return False
    if numero_str[0] == '-':
        numero_str = numero_str[1:]
    return all(c in '01' for c in numero_str)


"""
Multiplica cada dígito binario por la potencia de 2 correspondiente 
a su posición (empezando desde la derecha con la potencia 0) y luego suma los resultados.
"""


def binario_a_decimal(binario_str):
    decimal = 0
    potencia = 0
    if binario_str.startswith('-'):
        es_negativo = True
        binario_str = binario_str[1:]
    else:
        es_negativo = False

    for digito in reversed(binario_str):
        # Convertimos el dígito a entero antes de multiplicar
        decimal += int(digito) * (2 ** potencia)
        potencia += 1

    return -decimal if es_negativo else decimal


"""
Cada dígito binario se agrupa en conjuntos de 3 bits (desde la derecha) y 
cada grupo se reemplaza por su equivalente octal. Se pueden añadir ceros a la izquierda 
si es necesario para completar el último grupo de 3.
"""


def binario_a_octal(binario_str):
    tabla_bin_octal = {
        '000': '0', '001': '1', '010': '2', '011': '3',
        '100': '4', '101': '5', '110': '6', '111': '7'
    }

    es_negativo = False
    if binario_str.startswith('-'):
        es_negativo = True
        binario_str = binario_str[1:]

    # Asegurar que la longitud sea múltiplo de 3 para agrupar
    # Se añaden ceros a la izquierda si es necesario
    padding = len(binario_str) % 3
    if padding != 0:
        binario_str = '0' * (3 - padding) + binario_str

    octal = ""
    # Agrupar de 3 en 3 y convertir
    for i in range(0, len(binario_str), 3):
        grupo_3_bits = binario_str[i:i + 3]
        octal += tabla_bin_octal[grupo_3_bits]

    # Eliminar ceros a la izquierda, excepto si el resultado es solo '0'
    octal_final = octal.lstrip('0')
    if not octal_final:  # Si lstrip lo deja vacío (ej. "000" -> "0")
        octal_final = '0'

    return '-' + octal_final if es_negativo else octal_final


"""
Binario a Decimal: Multiplica cada dígito binario por la potencia de 2 
correspondiente a su posición (empezando desde la derecha con la potencia 0) y suma los resultados.

Decimal a Hexadecimal: Divide sucesivamente el número decimal por 16 y anota los restos en orden inverso. 
Los restos que sean mayores o iguales a 10 se reemplazan por 
sus equivalentes hexadecimales (A=10, B=11, C=12, D=13, E=14, F=15).
"""


def binario_a_hexadecimal(binario_str):
    # Paso 1: Convertir binario a decimal (usando la función ya definida)
    decimal_val = binario_a_decimal(binario_str)

    if decimal_val == 0:
        return '0'

    hexadecimal = ''
    es_negativo = False

    if decimal_val < 0:
        es_negativo = True
        decimal_val = -decimal_val  # Trabajar con el valor absoluto para la conversión

    # Tabla de conversión de residuos a caracteres hexadecimales
    digitos_hex = "0123456789ABCDEF"

    # Paso 2: Convertir decimal a hexadecimal
    while decimal_val > 0:
        residuo = decimal_val % 16
        # Obtener el carácter hexadecimal del residuo
        hexadecimal = digitos_hex[residuo] + hexadecimal
        decimal_val //= 16

    return '-' + hexadecimal.upper() if es_negativo else hexadecimal.upper()