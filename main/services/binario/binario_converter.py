




# Verifica si el número es binario
def es_binario(numero_str):
    if not numero_str:
        return False
    if numero_str[0] == '-':
        numero_str = numero_str[1:]
    return all(c in '01234567' for c in numero_str)


# Convierte el Nro Ingresado como Cadena a un Nro Entero
nro_binario = int(nro_binario)

# Se guarda el binario original
binario_original = nro_binario

"""
Binario a Decimal
"""
# Se inicializa en 0 el Nro. Decimal y la Potencia

nro_decimal = 0
potencia = 0

# Mientras el binario sea Mayor a 0 continua el ciclo
# 1º Se extrae el resto
# 2º Al Nro Decimal se le suma el Resto multiplicado por la base elevado a la potencia correspondiente
# 3º A la Potencia le sumo 1 para el siguiente cálculo
# 4º Al Nro Binario le quito el resto

while nro_binario > 0:

    resto = nro_binario % 10
    nro_decimal = nro_decimal + resto * (2 ** potencia)
    potencia += 1
    nro_binario = nro_binario // 10

print(f"\nEl Número Binario {binario_original} convertido a Decimal es {nro_decimal}")


"""
Binario a Decimal
"""

# Paso 2: Decimal a Octal
octal = 0
multiplicador = 1
temp = decimal
while temp > 0:
    resto = temp % 8
    octal += resto * multiplicador
    multiplicador *= 10
    temp //= 8

print("Octal:", octal)

# Paso 3: Decimal a Hexadecimal
hex_map = "0123456789ABCDEF"
hexadecimal = ""
temp = decimal
while temp > 0:
    resto = temp % 16
    hexadecimal = hex_map[resto] + hexadecimal
    temp //= 16

if hexadecimal == "":
    hexadecimal = "0"

print("Hexadecimal:", hexadecimal)
