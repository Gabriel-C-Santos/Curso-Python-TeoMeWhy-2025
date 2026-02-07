# uso do else

idade = input("Digite a sua idade para descobrir se você pode consumir bebida alcoolica ou não: ")
idade = int(idade)
print()

if idade >= 18:
    print("Voce pode consumir bebida alcoolica.")
    print("Porém, beba com moderação")

else:
    print("Voce não pode beber!")
    print("Consuma outro tipo de bebida.")