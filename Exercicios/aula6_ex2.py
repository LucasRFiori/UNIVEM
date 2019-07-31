comp = float(input('Qual o comprimento do terreno?: '))
carros = (int)
if(comp != 0):
    esq = int(input('Quantas esquinas tem na rua? '))
    esq = esq * 2
    compr = comp - esq

    carros = compr / 5

    print('O numero de carros que pode ser acomodado nessa rua é igual a {} carros.'.format(int(carros)))