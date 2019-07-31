D1 = float(input('Veiculo 1 -Digite o a distancia a ser percorrida: '))
T1 = float(input('Veiculo 2 -Digite o tempo que ele percorreu:'))
D2 = float(input('Veiculo 1 -Digite o a distancia a ser percorrida: '))
T2 = float(input('Veiculo 2 -Digite o tempo que ele percorreu:'))
if(D1 != 0  and D2 != 0):
    v1 = D1 / T1
    v2 = D2 / T2
    if(v1 >= v2):
        print('O carro um foi mais rapido com {} km/h.'.format(v1))
    if(v2 >= v1):
        print('O carro dois foi mais rapido com {} km/h.'.format(v2))
