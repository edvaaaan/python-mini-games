import random 

print('Pedra = R, Papel = P, Tesoura = S')
jogador = str(input('Digite sua opção: '))

lista = ['R', 'P', 'S']
maquina = random.choice(lista)
print('A maquina escolheu: {}'.format(maquina))

if jogador == 'R' and maquina == 'S':
    print('Você venceu!')
elif jogador == 'P' and maquina == 'R':
    print('Você venceu!')
elif jogador == 'S' and maquina == 'P':
    print('Você venceu!')
elif jogador == 'R' and maquina == 'P':
    print('Você perdeu!')
elif jogador == 'P' and maquina == 'S':
    print('Você venceu!')
elif jogador == 'S' and maquina == 'R':
    print('Você venceu!')
else:
    print('Empate!')
