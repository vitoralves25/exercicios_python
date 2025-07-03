cont = 0
numeros = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte']


while True:
    num = int(input('Digite seu Número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
#while num < 0 or num > 20:
    print('Tente Novamente.')
print(f'O número digitado foi {numeros[num]}')








    
    

