soma = cont = quant = masculino = feminino =  0
resp = 'FfMm'
while resp in 'FfMm':

    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    cont += 1


    resp = str(input('Digite seu Gênero: [M/F]: ')).upper().strip()[0]
    if cont == 1:
        masculino = feminino = resp
    else:
        if resp == 'M' and 'F':
            masculino += 1
            feminino += 1
        else:
            print('Gênero Inválido')
       

print(f'Foram contados {cont} nomes ao todo')
print(f'{quant} nomes Masculinos')
print(f'{quant} nomes Femininos')
