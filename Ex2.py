def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def verifica(numero, sequencia):
    if numero in sequencia:
        print(f"O número {numero} pertence à sequência Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência Fibonacci.")

numero = int(input("Digite um número: "))
sequencia = fibonacci(numero)

print(verifica(numero, sequencia))