# Faça um programa que vende uma garrafa de água
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50



texto = """ Escolha uma opção de agua para comprar:

(1) Agua mineral natural: R$ 1,50
(2) Agua mineral com gas: R$ 2,50
Opção: """

opção = input(texto)

print()

if opção == "1":
    print("VocÊ deve pagar R$ 1,50")

elif opção == "2":
    print("Você deve pagar R$ 2,50")

else:
    print("Opção invalida, refaça a compra!")