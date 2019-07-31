angulo_1 = int(input("Informe o ângulo 1: "))
angulo_2 = int(input("Informe o ângulo 2: "))

if (angulo_1 + angulo_2) == 90:
    print("Os angulos sao complementares!")
elif (angulo_1 + angulo_2) == 180:
    print("Os angulos sao suplementares!")
else:
    print("Erro!")