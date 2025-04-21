from services.octal.octal_converter import es_octal, octal_a_decimal, octal_a_binario, octal_a_hexadecimal

if __name__ == "__main__":
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

        # Si ingresa "2" se inicia la peticion y validacion del numero binario
        if sistema_convertir == "2":
            entrada_octal = input("Ingrese un número entero en sistema binario (o 'salir' para terminar): ").strip()
            if entrada_octal.lower() == 'salir':
                print("Gracias por usar el convertidor!")
                programa_on = False

        # Aca va la logica/funciones de conversion del sistema BINARIO a todos los demas

        # Si ingresa "10" se inicia la peticion y validacion del numero decimal
        if sistema_convertir == "10":
            entrada_octal = input("Ingrese un número entero en sistema decimal (o 'salir' para terminar): ").strip()
            if entrada_octal.lower() == 'salir':
                print("Gracias por usar el convertidor!")
                programa_on = False

        # Aca va la logica/funciones de conversion del sistema DECIMAL a todos los demas

        # Si ingresa "16" se inicia la peticion y validacion del numero hexadecimal
        if sistema_convertir == "16":
            entrada_octal = input("Ingrese un número entero en sistema hexadecimal (o 'salir' para terminar): ").strip()
            if entrada_octal.lower() == 'salir':
                print("Gracias por usar el convertidor!")
                programa_on = False

        # Aca va la logica/funciones de conversion del sistema HEXADECIMAL a todos los demas
