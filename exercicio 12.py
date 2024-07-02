def pergunta_11():
    print ("BEM VINDO A VAGA DE EMPREGO")
    idade = float(input("DIGITE SUA IDADE: "))
    nacionalidade = input("DIGITE SUA NACIONALIDADE (EM MINUSCULO): ")                # digitar o lugar que voce nasceu
    experiencia = float(input("DIGITE QUANTOS ANOS DE EXPERIENCIA VOCE TEM: "))       # digitar os seus anos de experiencia na area
    if idade >= 18:                                                                 
        if nacionalidade == "brasileiro" or nacionalidade == "brasileira":            # se a nacionalidade nao for brasileira ou brasileiro voce nao esta aprovado para a vaga de emprego
             if experiencia >=2:                                                      # se anos de experiencia for menor que 2 voce nao esta aprovado para a vaga de trabalho
                 print ("VOCE FOI APROVADO PARA A VAGA DE EMPREGO")

    else:
        print ("/////           VOCE NAO TEM TODOS OS REQUISITOS PARA PASSAR NA VAGA DE EMPREGO           /////")
pergunta_11()