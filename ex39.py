from datetime import date

atual = date.today().year

print('Bem Vindo ao Alistamento Militar')

nome = str(input('Qual o seu nome? '))

ano_nascimento = int(input('Qual o seu ano de nascimento? '))

ano = atual - ano_nascimento
idade = ano_nascimento + 18

if ano < 18:
    idade2 = ano + 18
    print(f'Você está com {ano} e não está na idade certa para se alistar')
    print(f'Seu alistamento vai ser em {idade}')
    

elif ano == 18:
    print(f'Você está com {ano} e está no ano certo para servir')
    

elif ano > 18:
    idade1 = ano - 18
    print(f'Você está com {ano} e já passou da hora de se alistar')
    print(f'Você era pra ter se alistado há {idade1} atrás')
    print(f'Seu alistamento foi em {idade}')
print('Tenha um ótimo dia, Cidadão')