def removeritem(lista):
    lista1 = []
    for item in lista:
        if item not in lista1:                      #ele pega a variavel "lista" e ve se ela tem numero repetido, se tiver ele tira o numero e retorna para ver se tem mais algum numero repetido
            lista1.append(item)
    return lista1
lista = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 9, 9, 10, 10]
lista1 = removeritem(lista)
print(lista1)