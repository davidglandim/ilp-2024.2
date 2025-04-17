matriz = []

for _ in range(10):
    matriz_aux = [str(x) for x in input().split()]
    matriz.append(matriz_aux)

matriz.insert(10, [0] * 10)
matriz.insert(0, [0] * 10)

for linha in matriz:
    linha.insert(10, 0)
    linha.insert(0, 0)

for l in range(12):
    for c in range(12):
        if matriz[l][c] in [0, "*"]:
            continue

        if matriz[l - 1][c] == "*":
            matriz[l][c] = "p"
            continue

        if matriz[l + 1][c] == "*":
            matriz[l][c] = "p"
            continue

        if matriz[l][c - 1] == "*":
            matriz[l][c] = "p"
            continue

        if matriz[l][c + 1] == "*":
            matriz[l][c] = "p"
            continue

matriz.pop(0)
matriz.pop()

for linha in matriz:
    linha.pop(0)
    linha.pop()

for linha in matriz:
    print(*linha)