cont = maiores_de_18 = homem = mulheres_menores_de_20 =  0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]')).upper().strip()[0]

    if idade > 18:
        maiores_de_18 += 1
    if sexo == 'M':
        homem += 1
    elif idade < 20:
        mulheres_menores_de_20 += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break   
print(f'Foram cadastrados {maiores_de_18} pessoas maiores de 18')
print(f'Foram cadastrados {homem} homens')
print(f'Foram cadastrados {mulheres_menores_de_20} mulheres menores de 20')



    # Tem que saber aninhar da forma correta, qualquer erro de aninhar vai dar errado
    # Talvez não consiga fazer com for, porque com o for eu vou ter limites

    