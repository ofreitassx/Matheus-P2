def numeroprimo ():
     numero = int(input("DIGITE UM NUMERO: "))
     if numero <= 1:
         primo = False                        # se o numero for menor que 1 ele nao é primo
     else:
         primo = True 
    
     for i in range (2, int(numero**0.5) + 1):              #aqui é pra verificar se o numero é primo, se "i" for igual a 0 é falso
         if numero % i == 0:
             primo = False
             break
    
     if primo:
         print (f'{numero} É PRIMO')
     else:
         print (f'{numero} NÃO É PRIMO')
numeroprimo ()

