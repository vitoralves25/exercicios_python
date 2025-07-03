peso = int(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
divisao = peso / altura**2
if divisao < 18.5:
    print(f'Você está com {divisao:1f} de IMC e está abaixo do peso')
    print('Cuidado, você precisa ganhar massa muscular')

elif divisao >= 18.5 and divisao < 25:
    print(f'Você está com {divisao} de IMC e está no peso ideal')
    print('Parabéns, continue se cuidando')

elif divisao >= 25 and divisao < 30:

    print(f'Você está com {divisao} de IMC e está sobre peso')
    print('Cuidado, você está começando a ter índices de obesidade')

elif divisao >= 30 and divisao <= 40:
    print(f'Você está com {divisao} de IMC e está na obesidade')
    print('Cuidado, se cuide')
    
elif divisao > 40:
    print(f'Você está com {divisao} de IMC e está na Obesidade mórbica')
    print('cuidado, se cuide')
