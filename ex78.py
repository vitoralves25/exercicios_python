cont = 0
valores = []
maior = valores
menor = valores
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('>=' * 18)
print(f'Você digitou os valores {valores}')

for pos, v in enumerate(valores, ):
    if pos in valores:
        maior = max(valores)
    if pos in valores:
        menor = min(valores)
    if pos in valores:
        pos = v
print(f'O maior valor {maior} está na posição {pos}')
print(f'O menor valor {menor} está na posição {pos}')

    
#for v in valores:
    #print(f'Os valores são {v}')

        




        #print(f'O maior valor foi {max(valores)} na posição {pos}')
    #if min(valores) in valores:
        #print(f'O menor valor foi {min(valores)} na posição {pos}')


#print(f'O maior valor foi {max(valores)} na posição {pos} \nO menor valor foi {min(valores)} na posição {pos}')
