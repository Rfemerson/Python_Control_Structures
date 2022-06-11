# Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# — Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
print('\033[33m*-*-\033[m' * 9)
print('Confederação Nacional de Natação')
print('\033[33m*-*-\033[m' * 9)
ano = int(input('Digite seu ano de nascimento:'))
categoria = date.today().year - ano
if categoria <= 9:
    print('Você tem {} anos, sua categoria é MIRIM'.format(categoria))
elif categoria <= 14:
    print('Você tem {} anos, sua categoria é INFANTIL'.format(categoria))
elif categoria <= 19:
    print('Você tem {} anos, sua categoria é JUNIOR'.format(categoria))
elif categoria <= 25:
    print('Você tem {} anos, sua categoria é SÊNIOR'.format(categoria))
elif categoria > 25:
    print('Você tem {} anos, sua categoria é MASTER'.format(categoria))


