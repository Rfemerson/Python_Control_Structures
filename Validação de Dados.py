# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.
s = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while s not in 'MmFf':
    s = str(input('Sexo invalido. Por favor digite seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} validado com sucesso.'.format(s))


