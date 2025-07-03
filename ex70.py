print(20 * '~')
print('Casa de Parafusos')
print(20 * '~')
cont = total_gasto =  produtos_acima_valor = nome_produto_barato = soma = menor =  0
barato = ' '
while True:
    produto = str(input('Produto: '))
    preco_produto = int(input('Preço do Produto:R$ '))
    cont += 1

    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_acima_valor += 1

    if cont == 1 or preco_produto < menor:
        menor = preco_produto
        barato = produto
    

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    
    if opcao == 'N':
        break


print(20 * '~', 'Fim do Programa', 20 * '~')
print(f'Total de Gasto:R$ {total_gasto}')
print(f'Temos {produtos_acima_valor} produtos acima de R$1000,00')
print(f'O produto mais barato foi o {barato} que custa R${menor}')


