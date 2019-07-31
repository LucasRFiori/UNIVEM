ano = int(input("Informe o ano: "))

if (ano % 400 == 0) or ((ano % 4 == 0) and (ano % 100 != 0)):
    print("É bissexto!")
else:
    print("Nao é bissexto!")