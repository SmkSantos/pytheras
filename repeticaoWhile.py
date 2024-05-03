
from random import randint

# Repetição em While

numSort = randint(1,9)
print(numSort)
numeroEscolhido = int(input("Informe um número entre 1 e 20 "))
contador = 0
while numeroEscolhido != numSort and contador < 5:
    print('Escolha outro número, pois você errou!!')
    numeroEscolhido = int(input("Informe um número entre 1 e 20 "))
    contador = contador+1
print("Parabéns, você acertou!!")