try:
    temperatura = float(input("Ingrese la temperatura: "))
    unidad = input("Ingrese la unidad (C o F): ")

    if unidad == 'C' or unidad == 'c':
        temperatura_fahrenheit = temperatura * 9/5 + 32
        print(f"{temperatura}°C equivale a {temperatura_fahrenheit:.2f}°F")
    elif unidad == 'F' or unidad == 'f':
        temperatura_celsius = (temperatura - 32) * 5/9
        print(f"{temperatura}°F equivale a {temperatura_celsius:.2f}°C")
    else:
        print("Unidad no válida. Por favor, ingrese 'C' o 'F'.")
except ValueError:
    print("Entrada no válida. Asegúrese de ingresar una temperatura numérica.")
