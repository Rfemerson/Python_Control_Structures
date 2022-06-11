# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
print('\033[32m =*= \033[m' * 9)
print('''      \033[47m Exército Brasileiro \033[m
\033[47m Desculbra sua situação de alistamento \033[m''')
print('\033[32m =*= \033[m' * 9)
ano = int(input('Digite seu ano de nascimento:'))
idade = date.today().year - ano
if idade < 18:
    diferenca = 18 - idade
    print('Ainda falta {} ano(s) para você se alistar'.format(diferenca))
elif idade == 18:
    print('Seu alistamento é imediato! Apresentesse ao quartel militar mais próximo de sua residência imediatamente.')
elif idade > 18:
    passou = idade - 18
    print('''Sua data de alistamento passou a {} ano(s), procure o quartel militar mais próximo de sua residência
imediatamente.'''.format(passou))

