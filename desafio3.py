#Faça um programa que peça o primeiro nome do usúario. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"
#se tiver entre 5 e 9 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"

while True:
    nome = input('Digite o seu nome: ')
    qnts = len(nome)

    if qnts <= 4:
        print('Seu nome é curto! ')

    elif qnts >5 and qnts < 9:
        print('Seu nome é normal! ')

    else: print('Seu nome é muito grande! ') 