# uso do elif
idade = input("Digite a sua idade para descobrir se você pode consumir bebida alcoolica ou não: ")
idade = int(idade)
print()

if idade >= 70:
    print("Cuidado com a bebida!")
    print("Consulte um especialista.")

elif idade >= 18:
    print("Voce pode consumir bebida alcoolica.")
    print("Porém, beba com moderação")

elif idade == 17:
    print("Você está quase na idade permitida para beber.")
    print("Aguarde mais um pouco!")

else:
    print("Voce não pode beber!")
    print("Consuma outro tipo de bebida.")