cont = homem = maiores_18 = mulheres_menor_20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [F/M]:'))
    opcao = str(input('Quer continuar?[S/N]:'))
    if opcao =='n':
        break
    cont += 1
    if idade > 18:
        maiores_18 += 1
    if sexo =='m':
        homem += 1
    else:
        mulheres_menor_20 += 1
print(f'Maiores de 18: {maiores_18}')
print(f'Homens Cadastrados: {homem}')
print(f'Mulheres menores de 20 anos: {mulheres_menor_20}')