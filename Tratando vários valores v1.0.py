cont = n = total = 0
n = int(input('Digite um valor: '))
while n != 999:
    cont += 1
    total += n
    n = int(input('Digite um valor: '))
print('Foram digitados {} números.'.format(cont))
print('A soma entre os números digitados é igual a {}'.format(total))
