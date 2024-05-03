
# Operadores Aritméticos
"""
Soma: +
Sub= -
Mult= *
Div= /
Div inteira = //
Resto Div= %
Potencia = **

"""

valor_1 = float(input('Digite o primeiro valor'))
valor_2 = float(input('Digite o segundo valor'))

print(f'Soma: {valor_1 + valor_2}')
print(f'Subtração: {valor_1 - valor_2}')
print(f'Multiplicação: {valor_1 * valor_2}')
print(f'Divisão: {valor_1 / valor_2}')
print(f'Divisão Inteira: {valor_1 // valor_2}') # Não considera os números decimais
print(f'Resto da Divisão: {valor_1 % valor_2}')
print(f'Potência: {valor_1 ** valor_2}')

# Operadores Booleanos: Sempre devolverá TRUE ou FALSE

idade1 = 10
idade2 = 15
altura1 = 1.77
altura2 = 1.65
altura3 = altura2 # iguala uma variavel com o valor de outra


print(idade1 > idade2) # MAIOR A
print(idade1 <= idade2) # MENOR IGUAL A
print('Python' == 'python') # IGUAL A
print('banana' != 'abacaxi') # DIFERENTE A
print(altura1 >= altura2) # MAIOR IGUAL A
print(altura2 > altura3) # MAIOR A


verdade = True
falso = False

inVerdade = not(verdade)

e = not (verdade) == falso and not(falso)== verdade

print(verdade,falso,inVerdade,e)