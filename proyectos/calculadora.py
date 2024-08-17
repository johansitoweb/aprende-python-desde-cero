def calculadora():
    print("Bienvenido a la calculadora")
    print("Operaciones: suma, resta, multiplicacion, division, potencia, raiz")

    while True:
        operacion = input("Elige una operación (o 'salir' para terminar): ")
        if operacion == 'salir':
            break

        if operacion in ['suma', 'resta', 'multiplicacion', 'division', 'potencia', 'raiz']:
            num1 = float(input("Ingresa el primer número: "))
            if operacion != 'raiz':
                num2 = float(input("Ingresa el segundo número: "))

            if operacion == 'suma':
                resultado = num1 + num2
            elif operacion == 'resta':
                resultado = num1 - num2
            elif operacion == 'multiplicacion':
                resultado = num1 * num2
            elif operacion == 'division':
                resultado = num1 / num2
            elif operacion == 'potencia':
                resultado = num1 ** num2
            elif operacion == 'raiz':
                resultado = num1 ** 0.5

            print(f"El resultado es: {resultado}")
        else:
            print("Operación no válida.")

calculadora()
