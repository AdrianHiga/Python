while True:

    av1 = int(input('Primeira nota do aluno: '))
    av2 = int(input('Segunda nota do aluno: '))

    media = (av1 + av2) / 2
    print(f'A média entre {av1} e {av2} é igual a {media:.2f}')
    if media >= 5:
        print(f'Aluno aprovado')

    else: print('Reprovado')

    

