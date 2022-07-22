print('CALCULADORA:')
controle = " "
while (controle != "0"):
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")
    controle = input("Digite a opção desejada: ")
print("Calculadora Encerrada!")

#Juntar as partes!
var1 = float( input("Digite um número: ") )
var2 = float( input("Digite outro número: ") )

if controle == 1:
        print("O resultado da Soma é: ", var1 + var2)
elif controle == 2:
    print("O resultado da Subtração é: ", var1 - var2)
elif controle == 3:
    print("O resultado da Multiplicação é: ", var1 * var2)
elif controle == 4:
    if var2 == 0:
        print("Impossível dividir por zero")
    else:
        print("O resultado da Divisão é: ", var1 / var2)