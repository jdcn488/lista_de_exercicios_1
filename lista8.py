raio = int(input('digite o raio:'))
altura = int(input('digite a altura:'))
valor = 50
lata = 5
pintura = lata * 3
areab = 3.14 * (raio**2)
areal = 2* 3.14 * raio * altura
areat = (areab*2) + areal
custo = pintura * areat
quantlat = areat / pintura
print('O custo em R$: ' + (str(round(custo))))
print('A quantidade de latas e: ' +(str(round(quantlat))))