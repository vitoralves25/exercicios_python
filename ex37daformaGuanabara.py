num = int(input('Digite um Número inteiro: '))
conversao = int(input('''Qual número você quer para conversão?
                      [1] Binário
                      [2] Octal
                      [3] Hexadecimal
                      '''))
if conversao == 1:
    print(f'O Número {num} convertido para binário fica {bin(num)[2:]}')
elif conversao == 2:
    print(f'O número {num} convertido para Octal fica {oct(num)}')
elif conversao == 3:
    print(f'O Número {num} convertido para Hexadecimal fica {hex(num)}')
else:
    print('Opção inválida')