a = [2,7,20, 50]
b = a[:]
b[2] = 8
print(f'A letra A tem {a}. \nA letra b tem {b}')

# Nesse caso, eu fiz uma cópia do a  para o b. Então se eu quiser mudar um valor da lista. Somente o valor da variável que foi dada a cópia vai ser mudada