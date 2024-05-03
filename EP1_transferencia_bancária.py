

# Criar uma interface fake de uma transferência entre contas bancárias

"""
Apenas por estudos:

- Criar duas variaveis para simular conta: Pagador e Favorecido
- Criar variaveis para receber o valor que será transferido
- Criar lógica para retirar da conta do pagador
- Criar lógica para adicionar a conta do pagador

"""

pagador = int(input("Favor, digite o valor que tem em conta:\n"))
favorecido = 3480

valorTrans = int(input("Favor, informe o valor a ser transferido:\n"))

print(f"Ok, está sendo enviado R$ {valorTrans},00 para a conta do favorecido.\nSeu saldo é de: R${pagador-valorTrans},00.")
print("==================================================================================================================\n\n")
print(f"Olá, você recebeu a quantia de R${valorTrans},00.\nSeu saldo é de R${favorecido+valorTrans},00.\n\n\n\nSeu saldo anterior era de R${favorecido},00")
