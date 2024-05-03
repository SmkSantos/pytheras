

# Recebe e atribui nome

nome = input('Digite seu nome\n')

# Recebe e atribui CPF
documento = input('Digite seu CNPJ/CPF\n')


# Recebe e verifica idade
idade = int(input('Qual a sua idade?\n'))


# Informa mensagem caso for menor de idade
if idade < 18:
    print(f'\n{nome}, infelizmente você não poderá criar uma conta por ser menor de idade. Contate seus responsáveis legais e a agência.')
# Informa agencia conta
else:
    print('Sua agência é: 1293\nSua conta é: 189203 - 2')

# Informa Login e senha
    print(f'Seu login é {nome}_{documento}.\nE sua senha é: {documento}')