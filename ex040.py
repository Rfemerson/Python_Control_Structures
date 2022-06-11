# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida: Média abaixo de 5.0: REPROVADO Média entre 5.0 e 6.9: RECUPERAÇÃO Média 7.0 ou
# superior: APROVADO
nota1, nota2 = input('Digite suas notas:').split()
nota1 = float(nota1)
nota2 = float(nota2)
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média foi {}. Sinto muito, você foi REPROVADO!'.format(media))
elif media == 5 or media <= 6.9:
    print('Sua média foi {}, Você está de recuperação!'.format(media))
elif 7 <= media:
    print("Sua média foi {}, Você foi APROVADO!".format(media))

