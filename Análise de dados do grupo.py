maior18 = quanthomens = mulhermenor20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        quanthomens += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1
    if opcao == 'N':
        print(f'''{maior18} Pessoas cadastradas tem mais do que 18 anos.
        {quanthomens} homens foram cadastrados.
        {mulhermenor20} Mulheres com menos de 20 anos foram cadastradas''')
        break
