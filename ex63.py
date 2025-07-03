
print('=>' * 20)
print('Sequência De Fibonacci')
print('<=' * 20)

n = int(input('Digite um número: '))

t1 = 0
t2 = 1

print(f'{t1} => {t2}', end=' ')

cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'=> {t3}', end=' ')
    t1 = t2  # foi somando ao lado t1 + t2, indo pra outra na sequência
    t2 = t3  # foi somando ao lado t2 + t3, indo pra outra na sequência
    cont += 1


