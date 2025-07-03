cont = 0
par = 2
from random import randint
num = int(input('Digite um número: '))
segundo_num = int(input('Digite um segundo número: '))
terceiro_num = int(input('Digite um terceiro número: '))
quarto_num = int(input('Digite o quarto número: '))

tupla = (num, segundo_num, terceiro_num, quarto_num)
print(f'Você digitou esses números {tupla}')
#   for pos in tupla:
if 9 in tupla:
    cont += 1
    print(f'O Número 9 foi exibido {cont} vez')
elif 9 not in tupla:
    print('O número 9 não foi exibido na listagem')
if 3 in tupla:
    resultado = tupla.index(3)
    print(f'O 3 está na posição {resultado}* posição do índice')
elif 3 not in tupla:
    print('Não tem nenhum valor 3 na lista')

for pos in tupla:
    if pos % 2 == 0:
        print(f'O número {pos} é par')
    else:
        print(f'O número {pos} é impar')   





