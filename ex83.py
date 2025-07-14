expressao = str(input('Digite sua expressão: '))
lista = []
for simb in expressao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão Válida')
else:
    print('Expressão Inválida')