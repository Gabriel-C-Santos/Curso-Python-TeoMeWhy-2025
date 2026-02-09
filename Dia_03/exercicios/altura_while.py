# Faça um programa que receba 4 alturas
#  usando um laço de repetição e
#  realize a soma dessas alturas.

soma = 0 # valor final
qtde_entradas = 4 # contador de entradas

while qtde_entradas > 0:
    altura = input("digite a medida de uma altura em cm: ")
    altura = float(altura)
    soma += altura
    qtde_entradas -= 1

print("A soma das 4 alturas é de:", soma,"cm")

    