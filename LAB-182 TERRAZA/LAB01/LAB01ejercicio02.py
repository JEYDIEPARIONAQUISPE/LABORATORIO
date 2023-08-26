n = int(input("Ingrese un número: "))

numeros_primos = []

for num in range(2, n):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        numeros_primos.append(num)

print(f"Los números primos menores que {n} son: {numeros_primos}")
