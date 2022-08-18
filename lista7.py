hora = int(input('digite a hora:'))
min = int(input('digite os minutos:'))
seg = int(input('digite os segundos:'))
minseg = min * 60
horamin = hora * 60
horaseg = horamin * 60
totseg = seg + minseg + horaseg
totmin = min + horamin
print('O total dos minutos e:'+str(totmin))
print('O total dos segundos e:'+str(totseg))