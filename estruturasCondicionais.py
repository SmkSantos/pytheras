

'''idade = 10

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você não é maior de idade")'''


print("Olá, caro estudante! Tudo bem? \nMe informa suas notas dos 4 bimestres para que possa já receber o certificado de aprovação.")

bim1= float(input("Digite a sua nota do primeiro bimestre\n"))
bim2= float(input("Digite a sua nota do segundo bimestre\n"))
bim3= float(input("Digite a sua nota do terceiro bimestre\n"))
bim4= float(input("Digite a sua nota do quarto bimestre\n"))

notaFinal = ((bim1+bim2+bim3+bim4)/4)

if notaFinal > 5.5 and notaFinal < 6.5:
    print(f"Sua média é de: {notaFinal}\nVocê está de Recuperação")
elif notaFinal <= 5.5:
    print(f"Sua média é de: {notaFinal}\nVocê reprovou")
else:
    print(f"Você passou, meus parabéns.\nSua média é de: {notaFinal}\nSeu certificado é de: 'APROVADO'")


media = 5
presença= 100

if media > 7 and presença > 50:
    print("Aprovado")
else:
    print("Reprovado")