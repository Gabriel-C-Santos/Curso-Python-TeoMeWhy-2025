# Faça um programa que receba um número inteiro e
# calcule sua raiz quadrada e exiba o resultado.

numero = input("digite um numero inteiro para calcular e exibir a sua raiz quadrada: ")

numero = int(numero)

raiz = numero ** (1/2) # ou 0.5

raiz = round (raiz, 2)

print("a raiz quadrada do numero", numero, "é:", raiz)