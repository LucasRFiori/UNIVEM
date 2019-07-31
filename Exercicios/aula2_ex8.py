tempo = int(input("Informe o tempo em segundos: "))
segundos = tempo % 60
minutos = (tempo / 60) % 60
hora = (tempo / 60) / 60
print("{} hora(s), {} minuto(s) e {} segundo(s)".format(int(hora), int(minutos), int(segundos)))