num = cont = s = 0
while True:
    num = int(input('Digite um número, ou "999 para parar": '))
    if num == 999:
        break
    cont += 1
    s += num
print(f'Foram contados {cont} números e a soma total foi {s}')