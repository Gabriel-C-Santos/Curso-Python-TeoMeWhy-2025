# Escreva um programa que receba uma lista de números do usuário
#  e conte quantas vezes um número específico aparece na lista.
#  Solicite ao usuário um número e exiba a contagem.

lista = [1, 2, 3, 1, 1, 2, 4, 6, 5, 7, 3, 7, 8, 1, 9, 6]

numero = input("Entre com um número: ")
numero = int(numero)

contador = 0

for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de: ", numero, ":", contador)
