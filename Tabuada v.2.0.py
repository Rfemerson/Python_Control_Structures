#  Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número:'))
print('A tabuada de {}:'.format(n))
for c in range(0, 11):
    t = n * c
    print('{} * {} = {}'.format(n, c, t))


