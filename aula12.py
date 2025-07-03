#nome=str(input('Digite seu nome:'))
#if nome == 'Vitor':
 #   print('Que nome genial, parábens')
#elif nome in  ' Alves Bazeth':
 #   print('Parábens por esse nome lindo')
#elif nome == 'Raynara':
   # print('Que nome feminino lindo de se pronunciar')
#else:
#    print('Que nome normal')
#print('Tenha uma ótima tarde, beijos')

#marca=str(input('Digite sua marca:'))
#if marca == 'Nike':
 #   print('Que marca genial')
#elif marca =='Adidas':
  #  print('Que marca linda')
#elif marca in 'Puma marca bazeth':
 #   print('Nome genial para uma marca')
#else:
 #   print('Não tenho em mente nenhuma marca')
#print('Obrigado por consultar a mim')

from time import sleep
gps=str(input('Para onde você quer ir?'))
sleep(2)
print('Localizando...')
if gps =='Casa':
    print('Siga para a rua Infantino, depois vire a direita e chegará a sua casa')
elif gps=='Praça':
    print('Siga em direção a rua do meio, depois siga em frente e chegará à praça')
elif gps=='Praça':
    print('Siga reto em direção à Rodovia Presidente Dutra, chegando na dutra dirija à 100 metros e depois vire a direita na rua Infantes')
else:
    print('Rodovia em obra')
    print('Melhor achar outro local para ir')