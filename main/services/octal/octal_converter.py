def es_octal(numero_str):
    """Verifica si una cadena representa un número octal válido."""
    if not numero_str:
        return False
    if numero_str[0] == '-':
        numero_str = numero_str[1:]
    return all(c in '01234567' for c in numero_str)

def octal_a_decimal(octal_str):
    """Convierte un número octal (string) a decimal (entero)."""
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

def octal_a_binario(octal_str):
    """Convierte un número octal (string) a binario (string)."""
    tabla_octal_bin = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }
    binario = ""
    if octal_str.startswith('-'):
        binario += '-'
        octal_str = octal_str[1:]
    for digito in octal_str:
        binario += tabla_octal_bin[digito]
    return binario.lstrip('0') if len(binario) > (1 if binario.startswith('-') else 0) else '0'

def octal_a_hexadecimal(octal_str):
    """Convierte un número octal (string) a hexadecimal (string)."""
    decimal_val = octal_a_decimal(octal_str)
    return hex(decimal_val)[2:].upper() if decimal_val != 0 else '0'