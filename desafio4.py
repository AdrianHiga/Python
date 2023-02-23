import os

lista = []
contador = 0
qts = 0
while contador < 5:
    print('Lista de compra, selecione uma opção: ')
    opcoes = input('[i]nserir [a]pagar l[listar]')

    if opcoes == 'i':
        os.system('cls')
        contador += 1
        qts +=1
        valor = input('O que deseja adicionar? ')
        lista.append(valor)
        

    elif opcoes == 'a':
        os.system('cls')
        indice_apagar = input('Digite o indice que deseja apagar: ')

        try:
            indice = int(indice_apagar)
            contador =- 1
            qts =-1
            del lista[indice]
            
        except:
            pass

    elif opcoes == 'l':
        os.system('cls')
        for i, valor in enumerate(lista):
            print(i, valor)

print(f'Esse mês vc irá comprar {lista}')
print(f'Quantidade {qts}')

