primeira_nota = float(input('Qual a nota do primeiro aluno? '))
segunda_nota = float(input('Qual a nota do segundo aluno? '))
media = 10 / 2
if primeira_nota and segunda_nota < 5.0:
    print('Aluno Reprovado')
elif primeira_nota and segunda_nota == 5.0 or primeira_nota and segunda_nota < 7.0:
    print('Aluno de Recuperação')
elif primeira_nota and segunda_nota == 7.0 or primeira_nota and segunda_nota > 7.0:
    print('Aluno Aprovado')