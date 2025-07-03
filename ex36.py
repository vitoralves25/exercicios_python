# Descrição: Programa que cálcula um valor de uma casa e verifica se o salário do comprador é suficiente para comprar

#Dessa outra forma fiquei um pouco travado
valor_casa = int(input('Qual o valor da casa? R$'))

salario = int(input('Qual o seu salário? R$'))

anos = int(input('Quantos anos vai querer pagar a casa?'))

prestacao = valor_casa / (anos * 12) #48000 esse valor só vai ser isso se o valor da casa for 200000 e o ano for 50 anos

print(f'Para pagar a casa em R${valor_casa:.2f} em {anos}anos, a prestação será de {prestacao:.2f}')

minimo_salario = salario * 30 / 100  # 30% do salário equivale a 30/100

#Se esse salário for equivalete a 4000 o final vai ser 1200, que é o valor que ele vai permancer do salário pagando a casa

print(f'A prestação será de R${prestacao:.2f} e o minímo do salário será de R{minimo_salario}')

if prestacao <= minimo_salario:
    print('Financiamento Aprovado com sucesso')
else:
    print(f'Financiamento negado')







#if pagamento > prestacao
    #print('Financiamento da casa correto')
    #print('Financiamento aprovado')
#elif prestacao > pagamento:
    #print(f'Financiamento inválido, pois o  salário por mês será de {pagamento}, e vai exceder o salário')
#else:
    #print('Nome ou valor incorreto')
