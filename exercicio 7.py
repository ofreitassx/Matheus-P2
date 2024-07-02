def addlista ():
    lista = []
    while True:
         item = input("DIGITE OS ITENS DA SUA LISTA (escreva 'fim' para parar): ")
         if item == 'fim':                                     # se o usuario escrever "fim" o programa para de adicionar os item na lista
              break
    
         lista.append(item) # pra adicionar os itens na lista
    print (lista)
addlista ()
