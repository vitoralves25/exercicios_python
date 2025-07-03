nome = str(input('Qual o nome completo do atleta? '))
ano_nascimento = int(input('Qual o seu ano de nascimento? '))
idade = 2025 - ano_nascimento
if idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 20:
    print('Categoria: Sênior')
elif idade > 20:
    print('Acima: Master')