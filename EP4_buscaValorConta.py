

# Cria 2 listas com valores
# Faça soma de índice
# Faça multiplicação de indice
# Gere uma condicional para buscar se valor é par

listaA, listaB = [1,2.4,4.4,10,53],[1.1,3.3,91.3,8,-9]
soma = 0
for valor in listaA:
    for valor2 in listaB:
        print(f'Soma anterior é: {soma}')
        soma = valor + valor2
        print(f'A soma entre {valor2} com a soma anterior é: {soma}\n')


valorFinalSoma = soma
print(f'VALOR FINAL DA SOMA É: {valorFinalSoma}')
multiplicacao = 0

for valor in listaA:
    for valor2 in listaB:
        print(f'Multiplicação anterior é: {multiplicacao}')
        multiplicacao = valor * valor2
        print(f'A multiplicação entre {valor2} com a multiplicação anterior é: {multiplicacao}\n')

valorFinalMult = multiplicacao
print(f'VALOR FINAL DA MULTIPLICAÇÃO É: {valorFinalMult}')

if valorFinalMult % 2 == 0:
    print('Multiplcação é par')
else:
    print('Multiplcação é impar')

if valorFinalSoma % 2 == 0:
    print('Soma é par')
else:
    print('Soma é impar')
