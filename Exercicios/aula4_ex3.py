print("Amigo 1")
amigo_1 = int(input("Informe o valor 2 ou 1: "))
print("Amigo 2")
amigo_2 = int(input("Informe o valor 2 ou 1: "))
print("Amigo 3")
amigo_3 = int(input("Informe o valor 2 ou 1: "))

if (amigo_1 != amigo_2) and (amigo_1 != amigo_3):
    print("Amigo 1 vencedor.")
elif amigo_2 != amigo_1 and amigo_2 != amigo_3:
    print("Amigo 2 vencedor.")
elif amigo_3 != amigo_1 and amigo_3 != amigo_2:
    print("Amigo 3 vencedor.")
else:
    print("Empate.")