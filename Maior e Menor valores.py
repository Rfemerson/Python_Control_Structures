resp = 'S'
num = total = cont = maior = menor = 0
while resp in 'S':
    num = int(input('Digite um valor: '))
    resp = str(input('Você quer continuar? [S/N] ')).upper().split()[0]
    total += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print('A média entre os valores digitados é igual a {}'.format(total / cont))
print('O naior valor digitado foi {} e o menor foi {}'.format(maior, menor))


