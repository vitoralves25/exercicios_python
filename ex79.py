valores = []
cont = 0
while True:
    numeros = int(input('Digite seu Número: '))
    if numeros not in valores:
        valores.append(numeros)
        print('Valor adicionado com sucesso')
    elif numeros in valores:
        print('Valores duplicados não podem ser adicionados')



    resposta = 'SsNn'
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
    cont += 1
valores.sort(reverse=True)
print(f'Foram cadastrados os valores {valores}')
    