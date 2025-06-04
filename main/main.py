from services.octal.octal_converter import es_octal, octal_a_decimal, octal_a_binario, octal_a_hexadecimal
from services.hexadecimal.hexadecimal_converter import conver_hexa_octal, conver_hexa_deci, conver_hexa_bin, \
    es_hexagonal
from services.decimal.decimal_converter import es_decimal, decimal_a_octal, decimal_a_binario, decimal_a_hexadecimal
from services.binario.binario_converter import es_binario, binario_a_octal, binario_a_decimal, binario_a_hexadecimal


print("Bienvenido al Convertidor de sistemas númericos")
print("-" * 30)

programa_on = True
# Inicio del menu usuario
while programa_on:
    sistema_convertir = input("Seleccione la base del sistema del cual desea las conversiones (2 / 8 / 10 / 16 / "
                              "'salir' para terminar): ")

    if sistema_convertir.lower() == 'salir':
        print("Gracias por usar el convertidor!")
        programa_on = False

    # Se valida que ingrese valores correctos
    while (sistema_convertir != "2"
           and sistema_convertir != "8"
           and sistema_convertir != "10"
           and sistema_convertir != "16"
           and sistema_convertir != "salir"):
        sistema_convertir = input("El valor ingresado es incorrecto. Ingrese nuevamente una opcion valida (2 / 8 "
                                  "/ 10 / 16 /"
                                  "'salir' para terminar): ")

        if sistema_convertir.lower() == 'salir':
            print("Gracias por usar el convertidor!")
            programa_on = False

    # Si ingresa "8" se inicia la peticion y validacion del numero octal
    if sistema_convertir == "8":
        entrada_octal = input("Ingrese un número entero en sistema octal (o 'salir' para terminar): ").strip()
        if entrada_octal.lower() == 'salir':
            print("Gracias por usar el convertidor!")
            programa_on = False

        # Se valida que sea un numero octal valido, si lo es, se convierte a los de mas sistemas
        while True:
            if es_octal(entrada_octal):
                decimal = octal_a_decimal(entrada_octal)
                binario = octal_a_binario(entrada_octal)
                hexadecimal = octal_a_hexadecimal(entrada_octal)

                print("-" * 30)
                print(f"Número octal: {entrada_octal}")
                print(f"  - Decimal:     {decimal}")
                print(f"  - Binario:     {binario}")
                print(f"  - Hexadecimal: {hexadecimal}")
                print("-" * 30)
                break
            # Si no es un numero octal valido, se muestran mensajes explicativos
            else:
                print("-" * 30)
                print("Error! La entrada no es un número entero octal válido.")
                print("Un número octal solo puede contener dígitos del 0 al 7.")
                print("-" * 30)
                entrada_octal = input(
                    "Ingrese un número entero en sistema octal (o 'salir' para terminar): ").strip()
                if entrada_octal.lower() == 'salir':
                    print("Gracias por usar el convertidor!")
                    programa_on = False
                    break

    # Si ingresa "10" se inicia la peticion y validacion del numero decimal
    if sistema_convertir == "10":
        entrada_decimal = input("Ingrese un número entero en sistema decimal (o 'salir' para terminar): ").strip()
        if entrada_decimal.lower() == 'salir':
            print("Gracias por usar el convertidor!")
            programa_on = False

        # Se valida que sea un numero octal valido, si lo es, se convierte a los de mas sistemas
        while True:
            if es_decimal(entrada_decimal):
                octal = decimal_a_octal(int(entrada_decimal))
                binario = decimal_a_binario(int(entrada_decimal))
                hexadecimal = decimal_a_hexadecimal(int(entrada_decimal))

                print("-" * 30)
                print(f"Número decimal: {entrada_decimal}")
                print(f"  - Octal:     {octal}")
                print(f"  - Binario:     {binario}")
                print(f"  - Hexadecimal: {hexadecimal}")
                print("-" * 30)
                break
            # Si no es un numero decimal valido, se muestran mensajes explicativos
            else:
                print("-" * 30)
                print("Error! La entrada no es un número entero decimal válido.")
                print("Un número decimal solo puede contener dígitos del 0 al 9.")
                print("-" * 30)
                entrada_decimal = input(
                    "Ingrese un número entero en sistema decimal (o 'salir' para terminar): ").strip()
                if entrada_decimal.lower() == 'salir':
                    print("Gracias por usar el convertidor!")
                    programa_on = False
                    break

    # Si ingresa "16" se inicia la peticion y validacion del numero hexadecimal
    if sistema_convertir == "16":
        entrada_hexa = input("Ingrese un número entero en sistema hexadecimal (o 'salir' para terminar): ").strip()
        if entrada_hexa.lower() == 'salir':
            print("Gracias por usar el convertidor!")
            programa_on = False

        # Se valida que sea un numero octal valido, si lo es, se convierte a los de mas sistemas
        while True:
            if es_hexagonal(entrada_hexa.upper()):
                decimal = conver_hexa_deci(entrada_hexa)
                binario = conver_hexa_bin(conver_hexa_deci(entrada_hexa))
                octal = conver_hexa_octal(conver_hexa_deci(entrada_hexa))

                print("-" * 30)
                print(f"Número hexadecimal: {entrada_hexa}")
                print(f"  - Decimal:     {decimal}")
                print(f"  - Binario:     {binario}")
                print(f"  - Octal: {octal}")
                print("-" * 30)
                break
            # Si no es un numero hexadecimal valido, se muestran mensajes explicativos
            else:
                print("-" * 30)
                print("Error! La entrada no es un número entero hexadecimal válido.")
                print("Un número hexadecimal solo puede contener dígitos del 0 al 9 y letras de la 'A' a la 'F'.")
                print("-" * 30)
                entrada_hexa = input(
                    "Ingrese un número entero en sistema hexadecimal (o 'salir' para terminar): ").strip()
                if entrada_hexa.lower() == 'salir':
                    print("Gracias por usar el convertidor!")
                    programa_on = False
                    break


    # Aca va la logica/funciones de conversion del sistema BINARIO a todos los demas

"""
    # Si ingresa "2" se inicia la peticion y validacion del numero binario
    if sistema_convertir == "2":
        entrada_binaria = input("Ingrese un número entero en sistema binario (o 'salir' para terminar): ").strip()
        if entrada_binaria.lower() == 'salir':
            print("Gracias por usar el convertidor!")
            programa_on = False

        # Se valida que sea un numero binario valido, si lo es, se convierte a los de mas sistemas
        while True:
            if es_binario(entrada_binaria.upper()):
                octal = binario_a_octal(entrada_binaria)
                decimal = binario_a_decimal(entrada_binaria)
                hexadecimal = binario_a_hexadecimal(entrada_binaria)

                print("-" * 30)
                print(f"Número binario: {entrada_binaria}")
                print(f"  - Octal:     {octal}")
                print(f"  - Decimal:     {decimal}")
                print(f"  - Hexadecimal: {hexadecimal}")
                print("-" * 30)
                break
            # Si no es un numero binario valido, se muestran mensajes explicativos
            else:
                print("-" * 30)
                print("Error! La entrada no es un número entero binario válido.")
                print("Un número binario solo puede contener como dígitos el 0 o el 1")
                print("-" * 30)
                entrada_binaria = input(
                    "Ingrese un número entero en sistema binario (o 'salir' para terminar): ").strip()
                if entrada_binaria.lower() == 'salir':
                    print("Gracias por usar el convertidor!")
                    programa_on = False
                    break
"""
