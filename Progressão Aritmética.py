# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.
i = int(input('Digite o incio da P.A:'))
p = int(input('Digite a razão da P.A:'))
decimo = i + (10 - 1) * p
for c in range(i, decimo + p, p):
    print('{}'.format(c), end='-')
print('Fim!')
