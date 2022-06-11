cont = 0
while True:
    print('-' * 30)
    num = int(input("Qual valor deseja ver a tabuada? "))
    if num < 0:
        break
    print(f'A tabuada do número {num} é:')
    for cont in range(1, 11):
        print(f'{num} * {cont} = {num * cont}')
    cont += 1
    print('-' * 30)
print('PROGRAMA ENCERRADO!')
