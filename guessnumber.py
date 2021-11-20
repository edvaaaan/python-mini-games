from random import randrange

r = randrange(50)
while True:
    n = input('Digite um número de 0 a 50: ')
    if r == n:
        print('Você ganhou!')
        break
