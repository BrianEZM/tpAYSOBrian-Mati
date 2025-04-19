
from services.octal.octal_converter import es_octal, octal_a_decimal, octal_a_binario, octal_a_hexadecimal

if __name__ == "__main__":
    print("Bienvenido al Convertidor Octal")
    print("-" * 30)

    while True:
        entrada_octal = input("Ingrese un número entero en sistema octal (o 'salir' para terminar): ").strip()
        if entrada_octal.lower() == 'salir':
            print("¡Gracias por usar el convertidor!")
            break

        if es_octal(entrada_octal):
            decimal = octal_a_decimal(entrada_octal)
            binario = octal_a_binario(entrada_octal)
            hexadecimal = octal_a_hexadecimal(entrada_octal)

            print(f"Número octal: {entrada_octal}")
            print(f"  - Decimal:     {decimal}")
            print(f"  - Binario:     {binario}")
            print(f"  - Hexadecimal: {hexadecimal}")
            print("-" * 30)
        else:
            print("¡Error! La entrada no es un número entero octal válido.")
            print("Un número octal solo puede contener dígitos del 0 al 7.")
            print("-" * 30)
