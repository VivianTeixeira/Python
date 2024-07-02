'''
8) Desenvolva um programa que leia uma distância em metros e mostre os valores
relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72
A distância de 185.72m corresponde a:
0.18572Km
1.8572Hm
18.572Dam
1857.2dm
18572.0cm
185720.0mm
'''
metros = float(input('Digite uma distância em metros: '))
km = metros / 1000
hm = km * 10
dam = hm * 10
dm = dam * 100
cm = dm * 10
mm = cm * 10
print(f'{km}Km \n{hm}Hm \n{dam}Dam \n{dm:.1f}dm \n{cm}cm \n{mm}mm')