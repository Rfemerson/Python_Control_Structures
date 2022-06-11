# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
computador = randint(0, 10)
tentativas = 0
print('Vou pensar em um número de 0 a 10, você consegue advinhar? ')
jogador = int(input('Digite seu palpite: '))
print('HUUUUUM...')
sleep(3)
while computador != jogador:
    print('Não foi dessa vez! Tente novamente!')
    jogador = int(input('Digite seu palpite: '))
    tentativas += 1
    if computador == jogador:
        print('Você acertou! O computador pensou no número {} e você no número {}'.format(computador, jogador))
print('Você precisou de {} tentativa(s) para acertar'.format(tentativas))
