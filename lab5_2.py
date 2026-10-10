import math

D = float(input('Введіть діаметр кулі: '))

R = D / 2

xA = float(input('Введіть x точки A: '))
yA = float(input('Введіть y точки A: '))
zA = float(input('Введіть z точки A: '))

print()

xB = float(input('Введіть x точки B: '))
yB = float(input('Введіть y точки B: '))
zB = float(input('Введіть z точки B: '))

print()

xC = float(input('Введіть x точки C: '))
yC = float(input('Введіть y точки C: '))
zC = float(input('Введіть z точки C: '))

print()

print("A",(xA, yA, zA))
print("B",(xB, yB, zB))
print("C",(xC, yC, zC))

dA = math.sqrt(xA**2 + yA**2 + zA**2)
print('dA =', dA)
dB = math.sqrt(xB**2 + yB**2 + zB**2)
print('dB =', dB)
dC = math.sqrt(xC**2 + yC**2 + zC**2)
print('dC =', dC)

print('Радіус кулі дорівнює: ', R)

if dA <= R:
    print('Точка A належить кулі.')
else:
    print('Точка A не належить кулі')

if dB <= R:
    print('Точка B належить кулі.')
else:
    print('Точка B не належить кулі')

if dC <= R:
    print('Точка C належить кулі.')
else:
    print('Точка C не належить кулі')

