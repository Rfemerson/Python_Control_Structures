# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais
print('\033[33m=-=\033[m' * 7)
print('Comparador de números')
print('\033[33m=-=\033[m' * 7)
num, num1 = (input('Digite dois números:')).split()
num = int(num)
num1 = int(num1)
if num > num1:
    print('O valor {} é maior que o valor {}'.format(num, num1))
elif num1 > num:
    print('O valor {} é maior que o valor {}'.format(num1, num))
elif num == num1:
    print('Não existe valor maior, os dois são iguais')
