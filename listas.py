

# listas

notas = [5.5, 8, 9]

# criando listas

lista = [] # pode criar assim, por conta que no meio do código pode usar ela, ou seja, ela é um armário vazio criado agora, ao decorrer do código, vamos
# colocando coisas dentro dele

lista = list() # cria lista e converte estrutura em lista

#indices e slices(fatiamento)

listaDeLista = [12,'Samuel', 1.67, True]

print(listaDeLista[0])
print(listaDeLista[1])
print(listaDeLista[2])
print(listaDeLista[3])

# com negativo, ele realiza a busca de trás pra frente
print(listaDeLista[-1])

# slice

lista = [10,50,40,30, 25, 60, 59 ]

print(lista[0:3]) # pega do indice 0 até menor que o indice 3, lembrando  [0,1,2,3] => [10,50,40]
print(lista[4:7]) # pega do 4º índice até o indice menor que o 7º índice
print(lista[3:]) # le até o final a partir do 3º índice
print(lista[0:5:2]) # a partir do índice zero, leia de dois em dois até menor que o índice 5

# interagindo com for

for elemento in lista:
    print(f'Elemento: {elemento}.')


# interagindo com index ou lenght

print(f'O tamanho da lista é de aproximadamente {len(lista)}') # para pegar o comprimento da lista, usa-se o len(lista)

print('Nesse caso, temos que a numeração da lista assim:')

for index in range(len(lista)):  # usamos o range para executar dentro dessa numeração, se fosse lista, não precisaria do range. Como vimos acima.
    print(f' {index} - Elemento: {lista[index]}')
