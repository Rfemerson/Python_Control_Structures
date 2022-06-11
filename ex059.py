from time import sleep
s = 0
while s != 5:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    print('''Escolha a operação que deseja realizar:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    s = int(input('Opção: '))
    if s == 1:
        soma = n1 + n2
        print('Soma entre {} e {} é igual a {}.'.format(n1, n2, soma))
    elif s == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} e {} é igual a {} .'.format(n1, n2, multiplicacao))
    elif s == 3:
        if n1 > n2:
            print('O {} é maior do que {}.'.format(n1, n2))
        elif n1 < n2:
            print('O número {} é maior do que {}.'.format(n2, n1))
        elif n1 == n2:
            print('Os números {} e {} são iguais.'.format(n1, n2))
    elif s == 4:
        sleep(0.5)
print('Obrigado por utilizar nossa calculadora!')


