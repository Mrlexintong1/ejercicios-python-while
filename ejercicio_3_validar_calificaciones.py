# Ejercicio 3: Validar 15 calificaciones
valores = []
i = 0
while i < 15:
    cal = float(input(f"Ingrese calificación {i+1}/15 (0-5): "))
    if 0 <= cal <= 5:
        valores.append(cal)
        i += 1
    else:
        print("Valor inválido. Intente nuevamente.")
print("Calificaciones válidas registradas.")
