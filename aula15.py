n = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 10:
        break
    cont += 1
print(f'Foram contados {cont} números')