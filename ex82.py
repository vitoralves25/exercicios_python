valores = []
impar = []
par = []
cont =  0
while True:
    numeros = int(input('Digite um Número: '))
    

    if numeros not in valores:
        valores.append(numeros)
        if numeros % 2 == 0:
            par.append(numeros)
        elif numeros % 2 == 1:
            impar.append(numeros)
    
        
            
    


    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
    cont += 1
print(f'A lista completa é {valores}')
print(f'A lista dos impares são  {impar}')
print(f'A lista dos pares são {par}')

