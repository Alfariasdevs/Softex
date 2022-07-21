print('CALCULADORA:')
var1 = float( input("Digite um número: ") )
var2 = float( input("Digite outro número: ") )
operacao = int( input("Escolha a operação a ser executada: 1.Soma, 2.Subtração, 3.Multiplicação, 4.Divisão."))

if operacao == 1:
    print("O resultado da Soma é: ", var1 + var2)
elif operacao == 2:
    print("O resultado da Subtração é: ", var1 - var2)
elif operacao == 3:
    print("O resultado da Multiplicação é: ", var1 * var2)
elif operacao == 4:
    if var2 == 0:
        print("Impossível dividir por zero")
    else:
        print("O resultado da Divisão é: ", var1 / var2)
  
