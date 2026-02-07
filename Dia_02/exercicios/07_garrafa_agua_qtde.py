# Faça um programa que vende uma garrafa de água
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de garrafas de água



texto = """ Escolha uma opção de agua para comprar:

(1) Agua mineral natural: R$ 1,50
(2) Agua mineral com gas: R$ 2,50
Opção: """

opção = input(texto)

print()

valor_item = 0
if opção == "1":
    valor_item = 1.5
elif opção == "2":
    valor_item = 2.5


if valor_item == 0:
    print("Opção invalida, refaça a compra!")

else:
    qtde = input("Quantas garrafas? ")
    qtde = int(qtde)
    valor_total = valor_item * qtde
    print("O valor da sua conta é: R$", valor_total)