teste = []
teste.append('Vitor')
teste.append('Alves')
galera = []
galera.append(teste[:])
teste[0] = 'Raynara'
teste[1] = 'Silva'
galera.append(teste[:])
print(galera)

# Ou posso fazer a declaração de galera de outra maneira, Colocando colchetes dentro de colchetes, ou seja, lista dentro de lista


#galera = [['Vitor', 20], ['Raynara', 18], ['Carlos', 20], ['Inex', 21]]
#print(galera[0] [0], end=' ')
#print(galera[0] [1],'anos' ',' ' e', end=' ')
#print(galera[1] [0], end=' ')
#print(galera[1][1], 'anos')
#for p in galera:
    #print(f'{p[0]} tem {p[1]} de idade')


#galera = []
#idade = []
#totmaior = totmenor = 0
#for c in range(0,5):
#    galera.append(str(input('nome: ')))
#    idade.append(int(input('idade: ')))
#    galera.append(idade[:])
#    idade.clear()
#print(galera)

#for p in galera:
#    if p[1] >= 21:
#        print(f'{p[0]}')
#        totmaior += 1
#    if p[1] <= 21:
#        print(f'{p[0]}')
#        totmenor += 1

#print(galera)

