resp = 's'
i = 0
while resp == 's':
    print('1-Mikail Oscar Bellos.')
    print('2-Oscar Canhar.')
    print('Caio Rolando da Rocha.')
    voto = int(input('{}° eleitor - Digite o numero do seu voto:'.format(i + 1)))
    i = i + 1
    if(voto == 1 and voto != 0):
        print('-' * 100)
        print('Parabéns você votou em Mikail Oscar Bellos.')
        c1 = c1 + 1
        print('-' * 100)
    if(voto == 2 and voto != 0):
        print('-' * 100)
        print('Parabéns você votou em Oscar Canhar.')
        print('-' * 100)
        c2 = c2 + 1
    if (voto == 3 and voto != 0):
        print('-' * 100)
        print('Parabéns você votou em Caio Rolando da Rocha.')
        print('-' * 100)
        c3 = c3 + 1
    resp = str(input('Deseja votar em mais alguem? (s/n):'))
if(c1 >= c2 and c1 >= c3):
    print('Mikail Oscar Bellos ganhou a eleição com {} votos.'.format(c1))
if(c2 >= c1 and c2 >= c3):
    print('0scar Canhar ganhou a eleição com {} votos.'.format(c2))
if(c3 >= c1 and c3 >= c2):
    print('Caio Rolando da Rocha ganhou a eleição com {} votos.'.format(c3))