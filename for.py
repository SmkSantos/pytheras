

"""for variavel in range(10):   De 0 a 10
    print(variavel)
"""
"""for variavel in range(-99,11): de -99 até 10
        print(variavel)"""
"""
for variavel in range(1,10,2): de 1 a 10, com passo de 1 por 1 1,2 3[...],9
    print(variavel)"""


"""nota1 = float(input('Informe sua nota bim1'))"""

ajudante = 0
for i in range(1,4,1):
    print(i)
    nota = float(input(f'Informe sua nota {i}'))
    ajudante= ajudante + nota
    print(ajudante)
    media = ajudante/3

if media > 5.6:
    print('Passou!!')
elif media < 5:
    print('Reprovou')
else:
    print('Vá pra recuperação')



