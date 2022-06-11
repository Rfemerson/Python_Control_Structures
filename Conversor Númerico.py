# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
print('\033[31m=\033[m' * 20)
print('CONVERSOR NUMÉRICO')
print('\033[31m=\033[m' * 20)
x = int(input('Qual número deseja converter?'))
# print('Você deseja converter o número {} para qual base numérica?'.format(x))
print('''Para basa deseja converter?
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')
opçao = int(input('Sua opção:'))
if opçao == 1:
    print('O número {} em base binária é igual a {}'.format(x, bin(x)[2:]))
elif opçao == 2:
    print('O número {} em base octal é igual a {}'.format(x, oct(x)[2:]))
elif opçao == 3:
    print('O número {} em base hexadecima é igual a {}'.format(x, hex(x)[2:]))
else:
    print('Ops... Opção não encontrada! Retorne ao menu. ')
