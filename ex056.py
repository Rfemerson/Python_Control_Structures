# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaidade = 0
meida = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('---------- {}º PESSOA---------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:'))
    somaidade += idade
    if p == 1 and sexo == 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo == 'Mn' and maioridadehomen < idade:
        maioridadehomen = idade
        nomevelho = nome
    if sexo == 'Ff' and idade < 20:
        totmulher20 += 1
media = somaidade / 4
print('A média de idade do grupo é {}'.format(media))
print('O nome do homen mais velhor é {} e ele tem {] anos de idade.'.format(nomevelho, maioridadehomen))
print('Nessa lista temos {} mulheres com menos de 20 anos de idade'.format(totmulher20))



