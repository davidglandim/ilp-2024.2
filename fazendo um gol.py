zagueiro, goleiro = map(str, input().split())
drible, chute = map(str, input().split())

if (zagueiro == 'e' and drible == 'd') or (zagueiro == 'd' and drible == 'e'):
  print('Bloqueado')
else:
  print('Driblado')
  if (goleiro == 'e' and chute == 'd') or (goleiro == 'd' and chute == 'e'):
    print('...e o goleiro pega')
  else:
    print('Gol')