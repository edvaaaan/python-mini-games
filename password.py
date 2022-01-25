import random 

digitos = ['0','1','2','3','4','5','6','7','8','9']
letras_minusculas = ['a', 'e', 'i', 'o', 'u']
letras_maiusculas = ['A', 'E', 'I', 'O', 'U']

senha = random.choice(digitos) + random.choice(letras_minusculas) + random.choice(letras_maiusculas)

print(senha)