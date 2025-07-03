cont = 0
times = ['Flamengo', 'Botafogo', 'Palmeiras', 'Atlético Mineiro', 'Internacional', 'Vasco', 'Fluminense', 'Vitória', 'Grêmio', 'Fortaleza', 'São Paulo', 'Corinthians', 'Bahia', 'Santos', 'Cruzeiro', 'Sport', 'Juventude', 'Ceará', 'Mirassol', 'Chapecoense']
for time in range(1,len(times)):
    print(f'{time}^ {times[time]}')
    print('')
print(f'Os 5 primeiros são {times[0:5]}')
print('')
print(f'Os 4 últimos são {times[-4:]}')
print('')
print(f'Times em ordem alfabética: {sorted(times)}')
print('')

for c in range(1,len(times)):
    cont = 0
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}* Posição')

# Esse times.index foi usado para acessar a posição da chapecoense para exibir na tela
