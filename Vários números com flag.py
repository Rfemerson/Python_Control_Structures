soma = cont = 0
while True:
    n = int(input('Digite um número [999 PARA PARAR]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print('FIM!')
print(f'Você digitou {cont} números e a soma entre eles é igual a {soma}')

