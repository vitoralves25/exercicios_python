#numeros = [20, 10, 30, 50, 40]
#numeros.append(60)
#numeros.sort()
#numeros.insert(5,55)
#print(numeros)
#comprimento = len(numeros)
#print(f'O comprimento dessa lista é {comprimento}')

#numeros2 = [110, 70, 100, 90, 80]
#numeros2.sort(reverse=True)
#numeros2.insert(4,75)
#numeros2.append(65)
#print(numeros2)
#comprimento_maior_menor =len(numeros2)
#print(f'O comprimento dessa segunda lista é {comprimento_maior_menor}')

#if len(numeros) == len(numeros2):
#    print(f'Resultado correto')
#else:
#    print('Resultado errado')

#numeros3 = list(range(20,41))
#print(numeros3)
#print(' ')
#numeros4 = list(range(1,11))
#numeros4.sort(reverse=True)
#print(numeros4)
#

#par = impar =  0
#perg = 'SsNn'
#while True:
#    if len(numeros3) != numeros4:
#        perg = str(input('Você quer inserir um novo número na lista? [S/N]: ')).upper().strip()[0]
#        if perg == 'S':
#            novo_numero = int(input('Insira seu novo número: '))
#            if novo_numero % 2 == 0:
#                par += 1
#            elif novo_numero % 2 == 1:
#                impar += 1
#        elif perg == 'N':
#            break
#print('Fim do ciclo')
#print(f'Foram Inseridos {impar} números impares e {par} números pares')


numeros = []
numeros.append(10)
numeros.append(5)
numeros.append(20)
numeros.append(1)
numeros.append(2)
numeros.sort()
for pos, num in enumerate(numeros):
    print(f'Meu número está na posição {pos} e é o número {num}')

# a função enumerate me dá a posição(o índice do número) e o elemento na ordem que o número está
