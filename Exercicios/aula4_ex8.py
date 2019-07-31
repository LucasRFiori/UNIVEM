a = int(input("Informe o valor A: "))
b = int(input("Informe o valor B: "))
c = int(input("Informe o valor C: "))

if (a > b) and (a > c):
    print("A é o maior: {}".format(a))
elif b > c:
    print("B é o maior: {}".format(b))
else:
    print("C é o maior: {}".format(c))
