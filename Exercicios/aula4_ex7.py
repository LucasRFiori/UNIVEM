print("H - Homem ou M - Mulher")
sexo = str(input("Informe seu sexo: "))
altura = float(input("Informe sua altura: "))

if sexo == 'H':
    peso = (72.7 * altura) - 58
    print("Peso ideal: {:.2f}".format(peso))
elif sexo == 'M':
    peso = (62.1 * altura) - 44.7
    print("Peso ideal: {:.2f}".format(peso))
else:
    print("Erro!")