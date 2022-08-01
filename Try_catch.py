lista = [1,2,3,4,5,6]
numero = int(input(f'Digite um número entre 0 e {len(lista)-1}: '))
try:
    #se der certo
    print(lista[numero])
except:
    print('Algo deu errado.')