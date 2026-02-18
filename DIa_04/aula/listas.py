
# %%
idades = [28, 35, 42, 18, 50, 39, 25]

print(idades)
# %%

type(idades)

# %%
print(idades[0])

print(idades[4])
# %%
print("soma das idades =", sum(idades))

print("qtde idades=", len(idades))

print("média das idades =", sum(idades) / len(idades))

print("idade minima =", min(idades))

print("idade maxima =", max(idades))
# %%

Gabriel = ["Gabriel", "Coutinho", 25, 2000, ["Games", "Leitura", "Filmes", "Series"]]

print("Tamanho da lista Gabriel =", len(Gabriel))

print(Gabriel[4][0])
# ou
Hobbies = Gabriel[4]
Hobbie_1 = Hobbies[0]
print(Hobbie_1)

#ou

tamanho = len(Gabriel)
pos = tamanho - 1
Gabriel[pos][0]

Ultimo_Hobbie = Gabriel[pos]

Gabriel[pos][len(Ultimo_Hobbie) - 1]

Gabriel[-1][-2]
# %%

Gabriel[0:4] # intervalo aberto
# %%
Gabriel[3:]

# %%
Gabriel[4][-2:]
# %%
Gabriel[:4]
# %%
Gabriel[::2]

# Gabriel [start : stop : step]