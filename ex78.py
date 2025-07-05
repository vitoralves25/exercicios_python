valores = []
for pos, cont in enumerate(valores):
    valores.append(int(input('Digite um Número: ')))
print('=>' * 30)
print(f'O maior número digitado foi {max(valores)}, nas posições {pos}')
print(f'O menor número digitado foi {min(valores)}, nas posições {pos}')