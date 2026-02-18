

#idades = [17, 32, 56, 87]

#print(idades)

#idades.append(32)

#print(idades)

idades = []

while True:
    print("Entre com uma idade: ")

    if idades == "":
        break

    idades.append(int(idades))


print(idades)

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)


print("a média é: ", media) 
print("o valor minimo é: ", minimo) 
print("o valor maximo é: ", maximo) 
print("a quantidade de idades é: ", qtde) 