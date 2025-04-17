qtd_portas = int(input())
nivel = 1

for _ in range(qtd_portas):
  encontro, valor = input().split()
  valor = int(valor)

  if encontro == 'tesouro':
    nivel += valor

  elif encontro == 'monstro':
    print('Combate iniciado')
    if nivel >= valor:
      print('VITORIA')
      nivel += 1
    else:
      print('Derrota! Fim da aventura')
      break

  elif encontro == 'maldicao':
    if nivel - valor > 0:
      nivel -= valor
    else:
      nivel = 0

  if nivel >= 5:
    print('Aventura concluida')
    break