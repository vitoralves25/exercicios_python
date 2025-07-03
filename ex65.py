soma = quantidade = media = menor = maior = 0
resposta = 'S'

while resposta in 'Ss':
    num = int(input('Digite seu Número: '))
    soma += num
    quantidade += 1

    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = str(input('Você quer continuar? [S/N] ').upper().strip())

media = soma / quantidade
print(f'Foram contados {quantidade} números')
print(f'O maior número foi {maior}')
print(f'O menor número foi {menor}')










