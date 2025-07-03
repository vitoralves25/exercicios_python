produto = str(input('Qual o produto você vai querer? '))
condicao = str(input('Qual a forma de pagamento? '))
dinheiro = 10
cartao = 5
cartao_2 = 'normal'
cartao_3 = 20
juros = 20
if condicao == 'dinheiro':
    print(f'Você terá {dinheiro}% de desconto no produto')
elif condicao == 'cartão':
    print(f'Você terá {cartao}% de desconto no cartão')
elif condicao == '2 vezes no cartão de débito':
    print(f'Você terá um preço {cartao_2}')
elif condicao == '3x no cartão de crédito':
    print(f'Você terá {cartao_3}% de juros')
