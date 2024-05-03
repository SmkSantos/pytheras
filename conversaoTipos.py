

# Conversão de Tipos

idade = '26'
numero1 = '10'
numero2 = '20'

print(numero1+numero2) # 1020 - Concatena


print(idade, type(idade)) # Busca o tipo da var idade == Str

idade_inteira = int(idade)

print(idade, type(idade_inteira)) # Busca o tipo da idade == int

numero2_bool = bool(numero2)
print(numero2_bool, type(numero2_bool))

x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)