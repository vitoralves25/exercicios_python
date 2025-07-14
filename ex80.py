#lista = []
#for c in range(0,5):
#    numero = int(input('Digite seu Número: '))
#    
#    if c == 0 or numero > lista[len(lista)-1]:
#        lista.append(numero)
#        print('Número adicionado ao final da lista')
#    else:
#        posicao = 0
#        while posicao < len(lista):
#            if numero <= lista[posicao]:
#                lista.insert(posicao, numero)
#               print(f'Número adicionado na posição {posicao}')
#                break
#            posicao += 1
#print(f'Os números adicionados foram {lista}')





lista = []
for c in range(0,5):
    numero = int(input('Digite seu número: '))

    if c == 0 or numero > lista[len(lista)-1]:
        lista.append(numero)
        print('Número adicionado na última posição')
    else:
        posicao = 0
        while posicao < len(lista):
            if numero <= lista[posicao]:
                lista.insert(posicao, numero)
                print(f'Número adicionado na posição {posicao}')
                break
            posicao += 1
print(f'Foram adicionados {lista} números')





  
    