# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
i = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
termo = i
c = 1
while c < 10:
    print('{}'.format(termo), end=' ')
    termo += r
    c += 1
print('FIM!')

