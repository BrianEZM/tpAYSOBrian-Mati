def hexa_a_decimal(caracter):
    """Convierte un carácter hexadecimal a su valor decimal"""
    if caracter == '0':
        return 0
    elif caracter == '1':
        return 1
    elif caracter == '2':
        return 2
    elif caracter == '3':
        return 3
    elif caracter == '4':
        return 4
    elif caracter == '5':
        return 5
    elif caracter == '6':
        return 6
    elif caracter == '7':
        return 7
    elif caracter == '8':
        return 8
    elif caracter == '9':
        return 9
    elif caracter == 'A' or caracter == 'a':
        return 10
    elif caracter == 'B' or caracter == 'b':
        return 11
    elif caracter == 'C' or caracter == 'c':
        return 12
    elif caracter == 'D' or caracter == 'd':
        return 13
    elif caracter == 'E' or caracter == 'e':
        return 14
    elif caracter == 'F' or caracter == 'f':
        return 15
    else:
        return False


def conver_hexa_bin(decimal_total):
    dividendo = decimal_total
    num_binario = ''
    while dividendo > 0:
        residuo = dividendo % 2
        num_binario = str(residuo) + num_binario
        dividendo = dividendo // 2
    return num_binario
    # print(f'EL NUMERO DE HEXADECIMAL A BINARIO ES {num_binario}')


def conver_hexa_deci(numeroHexa):
    i = len(numeroHexa) - 1
    j = 0
    decimal_total = 0
    while i >= 0:
        numerodeci = hexa_a_decimal(numeroHexa[i])
        decimal_total = decimal_total + numerodeci * (16 ** j)
        i -= 1
        j += 1
    return decimal_total


def conver_hexa_octal(decimal_total):
    dividendo = decimal_total
    num_octal = ''
    while dividendo > 0:
        residuo = dividendo % 8
        num_octal = str(residuo) + num_octal
        dividendo = dividendo // 8
    return num_octal
    # print(f'EL NUMERO DE HEXADECIMAL A OCTAL ES {num_octal}')


"""
# Programa principal
numeroHexa = input("ingrese un numero hexadecimal por teclado")
opcion = int(input('Ingrese el sistema al que desea convertir 1 - Decimal  2 - Binario 3 - Octal'))
if opcion == 1:
    print(f'EL NUMERO DE HEXADECIMAL A DECIMAL ES {conver_hexa_deci(numeroHexa)}')
elif opcion == 2:
    conver_hexa_bin(conver_hexa_deci(numeroHexa))
elif opcion == 3:
    conver_hexa_octal(conver_hexa_deci(numeroHexa))
else:
    print('La opcion no existe, reinicie y vuelva a intentar')
"""