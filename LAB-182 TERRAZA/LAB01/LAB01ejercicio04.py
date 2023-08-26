n = int(input("Ingrese un número: "))

fibonacci = [0, 1]

while len(fibonacci) < n:
    next_term = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_term)

print(f"La serie de Fibonacci hasta el término {n} es: {fibonacci}")
