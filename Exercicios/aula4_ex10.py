a = int(input("Informe o valor A: "))
b = int(input("Informe o valor B: "))
c = int(input("Informe o valor C: "))

if a >= c:
    a, c = c, a
if a >= b:
    a, b = b, a
if b >= c:
    b, c = c, b

print("A = {}, B = {}, C = {}".format(a, b, c))
