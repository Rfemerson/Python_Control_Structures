print('=' * 20)
print('      E7 TECH')
print('=' * 20)
total = maior1000 = cont = menor = 0
prodbarato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    valor = int(input('Preço: R$ '))
    opcao = ' '
    cont += 1
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? ')).upper().strip()[0]
    if valor > 0:
        total += valor
    if valor > 1000:
        maior1000 += 1
    if cont == 1 or valor < menor:
        menor = valor
        prodbarato = produto
    if opcao == 'N':
        break
print(f'O total da sua compra é de R$ {total:.2f}')
print(f'{maior1000} Produtos custam mais do que R$ 1000,00 reias')
print(f'O prduto que custa o menor foi {prodbarato} e custa R$ {menor:.2f}')



