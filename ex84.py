galera = []
dado = []

acima_peso = abaixo_peso = cont = maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]

    galera.append(dado[:])

        
    dado.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
    cont += 1
print(f'{len(galera)} pessoas foram cadastradas')
for p in galera:
    if p[1] == maior:
        print(f'O maior peso foi de {maior}kg de {p[0]}')
for p in galera:
    if p[1] == menor:
        print(f'O menor peso foi de {menor}kg de {p[0]}')



    
