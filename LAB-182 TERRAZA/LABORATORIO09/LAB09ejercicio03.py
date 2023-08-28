import random
import string

try:
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    incluir_mayusculas = input("¿Incluir letras mayúsculas? (Sí: S, No: N): ").lower() == 's'
    incluir_minusculas = input("¿Incluir letras minúsculas? (Sí: S, No: N): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (Sí: S, No: N): ").lower() == 's'
    incluir_especiales = input("¿Incluir caracteres especiales? (Sí: S, No: N): ").lower() == 's'

    caracteres = ""
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    if not caracteres:
        print("Debe seleccionar al menos un conjunto de caracteres.")
    else:
        contraseña_generada = ''.join(random.choice(caracteres) for _ in range(longitud))
        print(f"Contraseña generada: {contraseña_generada}")
except ValueError:
    print("Entrada no válida. Asegúrese de ingresar valores numéricos para la longitud.")
