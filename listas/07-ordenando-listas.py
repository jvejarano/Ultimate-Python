numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

# usuarios = [
#     [4, "Chanchito"],
#     [1, "Felipe"],
#     [5, "Pulga"]
# ]
usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pûlga", 5]
]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)
