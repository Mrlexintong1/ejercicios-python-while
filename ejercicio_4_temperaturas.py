# Ejercicio 4: Promedio de temperaturas hasta -273°C
suma = 0
contador = 0

while True:
    temp = float(input("Ingrese temperatura en °C (-273 para terminar): "))
    if temp == -273:
        break
    suma += temp
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"Promedio: {promedio:.2f}°C")
else:
    print("No se ingresaron temperaturas válidas.")
