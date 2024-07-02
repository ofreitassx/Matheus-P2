def filadeatendimento ():
    filadeatendimento = []
    while True:
         print ("\nESCOLHA UMA OPÇÃO:")                                                #essa parte do codigo é para voce escolher qual opcao voce vai usar
         print ("1 - ADICIONAR CLIENTE")
         print ("2 - ATENDER CLIENTE")
         print ("3 - MOSTRAR FILA DE ATENDIMENTO")
         
         opcao = input("\nOPÇÃO ESCOLHIDA: ")

         if opcao == "1":                                                                    # se a opcao escolhida for 1 voce vai adicionar uma pessoa na lista
             cliente = input("\nDIGITE O NOME DO CLIENTE QUE ENTROU NA FILA: ")
             filadeatendimento.append (cliente)                                              #.append = adicionar pessoa na lista
             print (f'\ncliente {cliente} entrou na fila')                                   # aqui mosta o nome da pessoa que foi adicionado na lista e é armazenado
    
         elif opcao == "2":                                                                  # se a opcao escolhida for 2 voce vai atender um cliente que foi adicionado anteriormente na opcao 1
             if filadeatendimento:
                 clienteatendido = input ("\nDIGITE O NOME DO CLIENTE QUE FOI ATENDIDO E SAIU DA FILA: ")
                 clienteatendido = filadeatendimento.pop(0)                       #.pop = é para tirar o nome da pessoa na lista
                 print(f'cliente {clienteatendido} foi atendido e saiu da fila')  # e aqui vai mostrar a pessoa que voce acabou de atender
             else:
                 print ("FILA DE ATENDIMENTO VAZIA")           # se a lista estiver vazia vai aparecer que a lista esta vazia

         elif opcao == "3":                  # se a opcao escolhida for 3 voce vai ver os clientes que estao na fila
             print ('FILA DE ATENDIMENTO: ')
             for idx, cliente in enumerate (filadeatendimento, start =1):     #essa parte eu tive que pesquisar, mas ai vai aparecer todos os clientes da lista que voce adcionou na lista
                 print (f'{idx}. {cliente}')  

         else:
             print ("ERRO NA DIGITACAO OU OPCAO INVALIDA, TENTE NOVAMENTE")
filadeatendimento ()
