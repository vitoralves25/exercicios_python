cont = 0
n = 1
s = 0
while n != 999:
    n = int(input('Digite um Número: "999" para parar: '))
    if n != 999:
        cont += 1
        s += n
print(f'Foram contados {cont} números e o total da soma foi {s} ')

# Método meu acima