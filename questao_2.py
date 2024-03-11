fibonacci = [0, 1]
numero = int(input("Escolha um número inteiro, verificarei se faz parte da sequência de Fibonacci: "))

while fibonacci[-1] < numero:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if numero in fibonacci:
    print(f"{numero} faz parte da sequência de Fibonacci.")
else:
    print(f"{numero} não faz parte da sequência de Fibonacci.")
