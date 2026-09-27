import random
import csv
import os

history = []
jugadas_A = []
jugadas_B = []

A = ""
B = ""

A_points = 0
B_points = 0


def always_cooperate():
    return "C"


def always_deflect():
    return "D"

def always_random():
    return random.choice(["C", "D"])


def points():
    global A_points, B_points

    if A == "C" and B == "C":
        A_points += 3
        B_points += 3

    if A == "D" and B == "D":
        A_points += 1
        B_points += 1

    if A == "C" and B == "D":
        A_points += 0
        B_points += 5

    if A == "D" and B == "C":
        A_points += 5
        B_points += 0



numero_rondas = 100

for i in range(numero_rondas):

    # jugador A
    A = always_cooperate()
    jugadas_A.append(A)

    # jugador B
    B = always_random()
    jugadas_B.append(B)

    # calcular puntos
    points()

    # guardar información de esta ronda
    history.append([i + 1, A, B, A_points, B_points])



print(history)


# Ruta donde está este script
folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "history.csv")


# Crear el archivo CSV
with open(file_path, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Cabecera
    writer.writerow(["Ronda", "A", "B", "Puntos A", "Puntos B"])

    # Datos
    writer.writerows(history)


print(f"Archivo creado en: {file_path}")