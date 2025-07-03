lista = ('boneco', 'aprender', 'comprar', 'atirar', 'loja', 'seco', 'rua', 'estrada')
for palavra in lista:
    print(f'\nNa frase {palavra} temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
