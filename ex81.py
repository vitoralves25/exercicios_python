valores = []
cont = 0
while True:
    valores.append(int(input('Digite seu Número: ')))
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
    cont += 1
valores.sort(reverse = True)

print(f'Foram Digitados {len(valores)} números ')
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print(f'O 5 está na lista na posição {valores.index(5)}')
else:
    print(f'O 5 não está na lista')
