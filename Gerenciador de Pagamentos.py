# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros
preco = float(input('Digite o valor do produto: R$'))
cond = input('''Digite o número que se aplica a sua condição de pagamento:
[ 1 ] À vista no dinheiro ou cheque
[ 2 ] À vista no cartão de credito
[ 3 ] Em até 2X no cartão de credito
[ 4 ] Em 3x ou mais no cartão de credito''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    valor = preco - ((preco * 10) / 100)
    print('O preço do produto era R$ {}, a vista fica R$ {}'.format(preco, valor))
elif opcao == 2:
    valor = preco - ((preco * 5) / 100)
    print('O valor do produto era R$ {}. A vista no cartão de credito fica R$ {}'.format(preco,valor))
elif opcao == 3:
    print('Em 2x vezes no cartão o valor é o mesmo, R$ {}'.format(preco))
elif opcao == 4:
    valor = preco + ((preco * 20) / 100)
    print('Em 3x ou mais o preço aumenta 20 %. O preço era R$ {} parcelado é R$ {}'.format(preco, valor))
else:
    print('OPÇÂO INVALIDA RETORNE AO MENU.')