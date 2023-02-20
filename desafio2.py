#Faça um programa que pergunte a hora ao usúario e, baseando-se no horário descrito, exiba a saudação apropriada.
#Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
nome = input('Qual o seu nome? ')
hora = int(input('Digite um horário: '))
while True:

    if hora >= 0 and hora <=11:
        print(f'Olá {nome}, Bom dia!')
        break
    elif hora >= 12 and hora <=17 :
        print(f'Olá {nome}, Boa tarde!')
        break

    elif hora >= 17 and hora <=23:
        print(f'Olá {nome}, Boa noite! ')
        break