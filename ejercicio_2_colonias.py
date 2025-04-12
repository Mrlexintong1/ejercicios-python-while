# Ejercicio 2: Colonias de bacterias
a = 4
b = 10
dias = 0

while a < b:
    a *= 1.03
    b *= 1.015
    dias += 1

print(f'Se necesitarán {dias} días para que la colonia A alcance o supere a la colonia B.')
