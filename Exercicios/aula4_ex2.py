velocidade_permitida = int(input("Informe a velocidade permitida: "))
velocidade_carro = int(input("Informe a velocidade do carro: "))

if velocidade_carro > velocidade_permitida:
    print("Velocidade excedida em: {} km/h.".format(velocidade_carro - velocidade_permitida))
else:
    print("Velocidade permitida.")