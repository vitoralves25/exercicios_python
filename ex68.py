from random import randint
num = cont = s = par = impar = 0
p = 'Pp'
i = 'Ii'
print(20 * '=', 'Vamos Jogar Par ou Ímpar', 20 * '=')
while True:
    num = int(input('Digite um Valor: '))
    computador = randint(0,10)
    s = num + computador


    escolha = str(input('Você quer [P/I] ')).upper().strip()
    if s % 2 == 0:
        par += 1
    else:
        impar += 1
    if s % 2 == 0:
        print(f'Você jogou {num} e o computador jogou {computador} e o resultado foi {s} que é par')

    else:
        print(f'Você jogou {num} e o computador jogou {computador} e o resultado foi {s} que é ímpar')
  
    if perg== 'i':
    
#print(50 * '=')    



