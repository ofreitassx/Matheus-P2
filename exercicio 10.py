def perfeito (n):
    soma = sum(i for i in range (1, n) if n % i == 0)
    return soma == n
numero = int(input("DIGITE UM NUMERO: "))
if perfeito(numero):
    print(f'{numero} É UM NUMERO PERFEITO')
else:
    print (f' {numero} NAO É UM NUMERO PERFEITO')
