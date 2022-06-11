# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    ano = int(input('Digite seu ano de nascimento:'))
    maior = atual - ano
    if maior >= 18:
        maiores += 1
    else:
       menores += 1
print('Dos 7, {} são maiores e {} são menores'.format(maiores, menores))
