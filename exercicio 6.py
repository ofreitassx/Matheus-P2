def maioremenor (n):
    maior = max (n)          #se a variavel "n" for maior vai aparecer aqui
    menor = min (n)          #se a variavel "n" for menor vai aparecer aqui
    return maior, menor
numero = input("DIGITE UMA LISTA DE NUMEROS SEPARADOS: ")
n = list(map(int, numero.split ()))         #aqui ele converte a lista para numeros inteiros
maior, menor = maioremenor(n)
print (f'MAIOR: {maior}')
print (f'MENOR: {menor}')