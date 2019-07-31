A = int(input('Digite o inicio de uma sequencia: '))
B = int(input('Digite o final da sequencia: '))
if(A and B != 0):
    for i in range(A, B, 2):
        print("{:.2f}".format(i))
