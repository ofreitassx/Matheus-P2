soma = 0
while True:
    numero = float(input("DIGITE UM NUMERO (digite 0 para parar): "))
    if numero == 0:
        break
    soma += numero

print(f"A soma dos números digitados é: {soma}")