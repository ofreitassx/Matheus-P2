def deznumeros (): 
     numeros = []
     for i in range(10):
         numero = float(input(f'Digite o {i+1}º número: '))
         numeros.append(numero)
     soma = sum(numeros)
     print(f'A soma dos 10 números é: {soma}')
deznumeros ()