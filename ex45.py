import random
from time import sleep
jogo = str(input('Vamos brincar de Jokenpo? Sim ou Não?'))
print('Se sim, vamos lá')
minha_escolha = str(input('Escolha entre Pedra, Papel ou Tesoura:'))
pc = ['Pedra', 'Papel', 'Tesoura']
print('O pc vai escolher.......')
print('Processando...')
sleep(2)
a = (random.choice(pc)) # tem que adaptar uma variável para fazer com condição(if,elif or else)
print(a)
print('E o player vai escolher o......')
print('Processando...')
sleep(2)
print(f'Player escolheu.... {minha_escolha}')


if minha_escolha == a:
    print('Empate')

elif minha_escolha != a and minha_escolha == 'Pedra' and a == 'Tesoura':
    print('Player ganhou')

elif a != minha_escolha and a == 'Tesoura' and minha_escolha == 'Papel':
    print('Pc ganhou')
    
elif minha_escolha != a and minha_escolha == 'Papel' and a == 'Pedra':
    print('Player ganhou')

elif a != minha_escolha and a == 'Pedra' and minha_escolha == 'Tesoura':
    print('Pc ganhou')

elif a != minha_escolha and a == 'Papel' and minha_escolha == 'Pedra':
    print('Pc ganhou')
elif minha_escolha != a and minha_escolha == 'Tesoura' and a == 'Papel':
    print('Player ganhou')
else:
    print('Nome inválido')






