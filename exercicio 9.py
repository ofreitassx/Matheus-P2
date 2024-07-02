
print ("BEM VINDO A CALCULADORA")
print ("1 - SOMAR")
print ("2 - MULTIPLICAR")
print ("3 - DIVIDIR")
print ("4 - SUBTRAIR")
calculadora = input("DIGITE QUAL VOCE DESEJA USAR: ")
if calculadora == "1":
    n1 = float(input("DIGITE O PRIMEIRO NUMERO: "))
    n2 = float(input("DIGITE O SEGUNDO NUMERO: "))
    soma = n1 + n2
    print ("A SUA SOMA É: ", soma)

if calculadora == "2":
    n1 = float(input("DIGITE O PRIMEIRO NUMERO: "))
    n2 = float(input("DIGITE O SEGUNDO NUMERO: "))
    multiplicacao = n1 * n2
    print ("SUA MULTIPLICACAO É: ", multiplicacao)

if calculadora == "3":
    n1 = float(input("DIGITE O PRIMEIRO NUMERO: "))
    n2 = float(input("DIGITE O SEGUNDO NUMERO: "))
    dividir = n1 / n2
    print ("A SUA DIVISAO É: ", dividir)

if calculadora == "4":
    n1 = float(input("DIGITE O PRIMEIRO NUMERO: "))
    n2 = float(input("DIGITE O SEGUNDO NUMERO: "))
    diminuir = n1 - n2
    print ("A SUA SUBTRACAO É: ", diminuir)

