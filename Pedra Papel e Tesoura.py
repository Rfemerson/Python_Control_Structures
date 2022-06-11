# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
print('PEDRA, PAPEL, TESOURA!')
print('''Qual sua escolha?
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Qual sua jogada?'))
print('=+' * 10 )
if jogador == 1:
    print('Você jogou Pedra')
elif jogador == 2:
    print('Você jogou Papel')
elif jogador == 3:
    print('Você jogou Tesoura')
lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
print('O computador jogou {}'.format(pc))
print('=+' * 10)
if jogador == 1 and pc == 'Pedra':
    print('Empate! O pc escolheu {} e você escolheu Pedra '.format(pc))
elif jogador == 1 and pc == 'Papel':
    print('pc ganhou. O pc escolheu {} e você escolheu Pedra '.format(pc))
elif jogador == 1 and pc == 'Tesoura':
    print('Você ganhou. O pc escolheu {} e você escolheu Pedra'.format(pc))
elif jogador == 2 and pc == 'Pedra':
    print('Você ganhou. O pc escolheu {} e você escolheu Papel'.format(pc))
elif jogador == 2 and pc == 'Papel':
    print('Empate. O pc escolheu {} e você escolheu Papel'.format(pc))
elif jogador == 2 and pc == 'Tesoura':
    print('pc ganhou. O pc escolheu {} e você escolheu Papel'.format(pc))
elif jogador == 3 and  pc == 'Pedra':
    print('Você perdeu. O pc escolheu {} e você escolheu Tesoura'.format(pc))
elif jogador == 3 and pc == 'Papel':
    print('Você ganhou. O pc escolheu {} e você escolheu Tesoura'.format(pc))
elif jogador == 3 and pc == 'Tesoura':
    print('Empate! O pc escolheu {} e você escolheu Tesoura'.format(pc))
else:
    print('Opção invalida')


