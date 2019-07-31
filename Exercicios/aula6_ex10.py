while True:
	numero = int(input("Informe o valor do número: "))
	cont = 0
	
	if numero == 0:
		break
	while numero != 0:
		resto = numero % 10
		if int(resto) % 2 != 0:
			cont += 1
		numero = numero // 10
	print("A quantidade de ímpares é: {}".format(cont))