try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = int(input("Seleccione el número de la operación que desea realizar: "))
    
    if opcion == 1:
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcion == 2:
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcion == 3:
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Opción no válida. Por favor, seleccione una operación del 1 al 4.")
except ValueError:
    print("Entrada no válida. Asegúrese de ingresar números para los operandos y la opción de operación.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
