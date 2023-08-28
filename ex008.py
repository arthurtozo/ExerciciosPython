medida = float(input('Uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida/10
hm = medida/100
km = medida/1000
print(f'A medida de {medida}m corresponde a\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm\n{dam}dam\n{hm}hm\n{km}km')
print('A medida de {}m corresponde a\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm\n{}dam\n{}hm\n{}km'.format(medida, dm, cm, mm, dam, hm, km))