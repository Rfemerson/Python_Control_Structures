# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
print('''Vamos formar um triângulo? Preciso que me informe o
comprimento das restas''')
n1 = float(input('Primeira reta:'))
n2 = float(input('Segunda reta:'))
n3 = float(input('Terceira reta:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n3:
    print('Temos um tirângulo!')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Não é possivel formar um triângulo')


