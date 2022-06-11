# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.
i = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
termo = i
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{}'.format(termo), end=' ')
        termo += r
        c += 1
    print('PAUSA!')
    mais = int(input('Quantos termos mais você deseja ver? '))
print('FIM')
print('Você visualizou {} termos da P.A'.format(total))

