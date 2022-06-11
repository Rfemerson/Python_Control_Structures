from random import randint
from time import sleep
print('Você é bom no PAR ou IMPAR?')
sleep(1)
print('Vamos descobrir!')
sleep(1)
cont = 0
while True:
    opcao = str(input('Par ou Impar? [P/I]: ')).upper().split()[0]
    jogador = int(input('Digite sua jogada: '))
    comput = randint(0, 11)
    jogada = jogador + comput
    print('Uma')
    sleep(0.5)
    print('Duas')
    sleep(0.5)
    print('Meia e')
    sleep(0.5)
    print('Já')
    if opcao == 'P' and jogada % 2 == 0:
        cont += 1
        print(f'Você ganhou! o computador digitou {comput} e você digitou {jogador}, {comput} + {jogador} = {jogada}')
    elif opcao == 'P' and jogada % 2 != 0:
        print(f'Você perdeu,o computador digitou {comput} e você digitou {jogador}, {comput} + {jogador} = {jogada}')
        break
    elif opcao == 'I' and jogada % 2 != 0:
        cont += 1
        print(f'Você ganhou! o computador digitou {comput} e você digitou {jogador}, {comput} + {jogador} = {jogada}')
    elif opcao == 'I' and jogada % 2 == 0:
        print(f'Você perdeu,o computador digitou {comput} e você digitou {jogador}, {comput} + {jogador} = {jogada}')
        break
print(f'GAME OVER! Você ganhou {cont} vezes!')

