a = int(input("Informe o valor A: "))
b = int(input("Informe o valor B: "))

a, b = b, a

# Outra solução seria, criar uma variável auxiliar
# em nosso caso a variável auxiliar
# auxiliar = a
# a = b
# b = auxiliar

print("Valor da variável A: {} e variável B: {}".format(a, b))