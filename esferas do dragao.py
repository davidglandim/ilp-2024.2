qtd_esferas = int(input())
estrelas_esferas = list(map(int, input().split()))
estrelas_esferas = [item for item in estrelas_esferas if item <= 7]

estrelas_esferas.sort()
print(" ".join(map(str, estrelas_esferas)))
if len(estrelas_esferas) == 7:
  print("Saia Shenlong e realize o meu desejo")
else:
  print("Nao encontramos todas")