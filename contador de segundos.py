n = int(input())
horas = n // 3600
minutos = (n % 3600) // 60
segundos = (n % 3600) % 60
print(f'{horas}h {minutos}m {segundos}s')