import random

dinheiro = 100

# CARA OU COROA

def cara_ou_coroa(aposta, tentativa):
    cara_ou_coroa = ['cara', 'coroa']
    pc_couc = random.choice(cara_ou_coroa)

    print(f'O resultado foi {pc_couc} \n')

    if tentativa.lower() == pc_couc:
        global dinheiro
        dinheiro += (aposta * 2)
        print(f'Parabéns! Você ganhou R$ {aposta * 2} \n')
    else:
        print('Você perdeu! \n')


# ADIVINHE O NÚMERO DOS DADOS

def dados(aposta, tentativa):
    dado = random.randint(1, 6)
    
    print(f'O dado deu {dado} \n')

    if tentativa == dado:
        global dinheiro
        dinheiro += (aposta *2)
        print(f'Parabéns! Você ganhou R$ {aposta * 2} \n')
    else:
        print('Você perdeu! \n')


# PROGRAMA PRINCIPAL

print('Olá visitante seja bem-vindo! \n')
idade = int(input('Qual é sua idade ? '))

if idade < 18:
    print('VAZA!')

if idade >= 18:
    
    while dinheiro > 0:
        print('Vamos começar os jogos! \n')

        while True:
            try:
                aposta_tt = int(input('Vai apostar quanto ? '))
                break
            except ValueError:
                print('Digite um número valido! \n')
                continue

        if aposta_tt > dinheiro:
            print('Você não tem isso tudo! \n')
            continue
        else:
            print('Qual joguinho você vai escolher?')
            print('(1) -> Cara ou coroa \n(2) -> Jogar dados \n(3) -> Sair')
            escolha = int(input(''))

            if escolha == 1:
                print('CARA OU COROA! \n')
                dinheiro -= aposta_tt
                print('Qual vai ser? Cara ou coroa? ')
                tentativa_tt = str(input(''))

                if tentativa_tt.lower() == 'cara' or tentativa_tt.lower() == 'coroa':
                    print(cara_ou_coroa(aposta_tt, tentativa_tt))
                    print(f'Seu dinheiro atual é de R$ {dinheiro} \n')

            elif escolha == 2:
                print('NÚMERO DO DADO \n')
                dinheiro -= aposta_tt
                print('De 1 a 6, qual você acha que vai dar no dado? ')
                tentativa_tt = int(input(''))

                print(dados(aposta_tt, tentativa_tt))
                print(f'Seu dinheiro atual é de R$ {dinheiro} \n')

            elif escolha == 3:
                print('Foi cedo!')
                break