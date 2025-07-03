number = float(input('Você pode me dar um número inteiro? '))

conversao = int(input('Em qual base de conversão você deseja me falar para converter? se for Binária, digite 1, se for Octal, digite 2, se for hexadecimal, digite3: '))

print('Se a sua escolha for Binária e digitar 1, embaixo estará o cálculo do número inteiro que você me deu ') 
print('Se a sua escolha for octal e digitar 2, embaixo estará o cálculo do número inteiro que você me deu')
print('Se a sua escolha for hexadecimal e digitar 3, embaixo estará o cálculo do número inteiro que você me deu')

calculo = number / 2
resultado = number / 2  and number % 2 
resultado2 = number / 2 and number % 2 # Esse number % 2 vai te dar o resto da divisão de 2

calculo2 = number / 8
resultado3 = number / 8 and number % 8 
resultado3 = number % 8
resultado4 = number / 8 and number % 8
resultado4 = number % 8

calculo3 = number / 16
resultado5 = number % 16
resultado6 = number % 16

if conversao == 1 and number >= calculo and resultado == 0:
    print(f'Você tem um número em binário com o cálculo de {calculo} e o resto dele é {resultado}' )

elif conversao == 1 and resultado2 > 0:
    print(f'Você terá um número em binário com o cálculo de {calculo} e o resto será {resultado2}')

elif conversao == 2 and number >= calculo2 and resultado3 == number % 8 and resultado3 == 0:
    print(f'Estou te enviando um número inteiro em octal com o cálculo de {calculo2} e o resto dele com {resultado3}')

elif conversao == 2 and number >= calculo2 and resultado4 == number % 8 and resultado4 > 0:
    print(f'Estou te enviando um número inteiro em octal com o cálculo de {calculo2} e o resto dele com o {resultado4}')

elif conversao == 3 and number >= calculo3 and resultado5 == number % 16 and resultado5 == 0:
    print(f'Estou te enviando um número inteiro em hexadecimal com o cáluco de {calculo3} e o resto desse cálculo com o {resultado5}')

elif conversao == 3 and number >= calculo3 and resultado6 == number % 8 and resultado6 > 0:
    print(f'Estou te enviando um número inteiro em hexadecimal com o cálculo de {calculo3} e o resto desse número com o {resultado6}')

#print('Se a sua escolha for octal e digitou 2, embaixo estará o cálculo do número inteiro que você me deu')

#Base de conversão de outra forma
num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
      [1] converter para Binário
      [2] converter para Octal
      [3] converter para Hexadecimal
      ''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'{num} convertido para binário é igual a {bin(num)}')



