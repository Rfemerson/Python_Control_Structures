# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
i = int(input('Inicio do intervalo:'))
f = int(input('Fim do intervalo:'))
for c in range(i, f+1):
    if c % 2 == 0:
        print(c, end= ' ')
print('Esses são os números pares entre {} e {}.'.format(i, f))
