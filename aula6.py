# Exercicio de fixação IMC

# Formúla IMC=  PESO / (ALTURA X ALTURA)

nome = input('Digite o seu nome: ')
peso = input('Digite o seu peso: ')
altura = input('Digite a sua altura: ')

peso = int(peso)
altura = float(altura)
resultado = resultado_imc = peso / (altura*altura)



print(nome)
print(peso)
print(altura)
print(f'O seu IMC é {resultado:.2f}')