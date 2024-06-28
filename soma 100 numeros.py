def soma100numeros ():
    soma = 0                                            # soma = 0 porque ainda nao tem nenhum numero
    for i in range ( 1 , 101 ):                         # 1 e 101 porque se nao vai comecar com 0
        soma += i                                       # a cada "+=" vai somar os dois numeros anteriores
    print (f'A SOMA DOS 100 NÚMEROS É: {soma}')         
soma100numeros ()