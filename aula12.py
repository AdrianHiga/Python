#Listas em Python

#Ex 1
contador = 0
qnts = 0
compra = ''
nome = input('Digite o seu nome: ')
while contador < 2:
    lista = input('Digite sua lista: ')
    listaDeCompra = lista.split(' ')
    print(listaDeCompra)
    compra += lista
    qnts +=1
    print(f'Quantidade de produtos: {qnts}')
    print(compra)
    contador +=1

print(f"Comprar {compra}! ")
