import random
import csv
import os

history = []
jugadas_A = []
jugadas_B = []
jugadas_C = []

A = ""
B = ""
C = ""


A_points = 0
B_points = 0
C_points = 0


def always_cooperate():
    return "C"


def always_deflect():
    return "D"

def always_random():
    return random.choice(["C", "D"])

def tit_for_tat(ronda, jugador):
    if ronda == 0:
        return "C"
    else:
        if jugador == "A":
            if jugadas_B[i-1] == "C":
                return "C"
            elif jugadas_B[i-1] == "D":
                return "D"
        elif jugador == "B":
                if jugadas_A[i-1] == "C":
                    return "C"
                elif jugadas_A[i-1] == "D":
                    return "D"

def tit_for_tat_chill(ronda, jugador):  #solo va por mayoria, tirando a cooperar

    if ronda == 0:
        return "C"
    else:
        if jugador == "A":
            if jugadas_B[i-1] == "C" and jugadas_C[i-1] == "C":
                return "C"
            if jugadas_B[i-1] == "D" and jugadas_C[i-1] == "C":
                return "C"
            if jugadas_B[i-1] == "C" and jugadas_C[i-1] == "D":
                            return "C"
            if jugadas_B[i-1] == "D" and jugadas_C[i-1] == "D":
                            return "D"
        if jugador == "B":
            if jugadas_A[i-1] == "C" and jugadas_C[i-1] == "C":
                return "C"
            if jugadas_A[i-1] == "D" and jugadas_C[i-1] == "C":
                return "C"
            if jugadas_A[i-1] == "C" and jugadas_C[i-1] == "D":
                return "C"
            if jugadas_A[i-1] == "D" and jugadas_C[i-1] == "D":
                return "D"
        if jugador == "C":
            if jugadas_A[i-1] == "C" and jugadas_B[i-1] == "C":
                return "C"
            if jugadas_A[i-1] == "D" and jugadas_B[i-1] == "C":
                return "C"
            if jugadas_A[i-1] == "C" and jugadas_B[i-1] == "D":
                return "C"
            if jugadas_A[i-1] == "D" and jugadas_B[i-1] == "D":
                return "D"
    return


def tit_for_tat_nervioso(ronda, jugador):  #solo va por mayoria, tirando a deflectar

    if ronda == 0:
        return "C"
    else:
        if jugador == "A":
            if jugadas_B[i-1] == "C" and jugadas_C[i-1] == "C":
                return "C"
            if jugadas_B[i-1] == "D" and jugadas_C[i-1] == "C":
                return "D"
            if jugadas_B[i-1] == "C" and jugadas_C[i-1] == "D":
                            return "D"
            if jugadas_B[i-1] == "D" and jugadas_C[i-1] == "D":
                            return "D"
        if jugador == "B":
            if jugadas_A[i-1] == "C" and jugadas_C[i-1] == "C":
                return "C"
            if jugadas_A[i-1] == "D" and jugadas_C[i-1] == "C":
                return "D"
            if jugadas_A[i-1] == "C" and jugadas_C[i-1] == "D":
                return "D"
            if jugadas_A[i-1] == "D" and jugadas_C[i-1] == "D":
                return "D"
        if jugador == "C":
            if jugadas_A[i-1] == "C" and jugadas_B[i-1] == "C":
                return "C"
            if jugadas_A[i-1] == "D" and jugadas_B[i-1] == "C":
                return "D"
            if jugadas_A[i-1] == "C" and jugadas_B[i-1] == "D":
                return "D"
            if jugadas_A[i-1] == "D" and jugadas_B[i-1] == "D":
                return "D"
    return



    return 
def alvector():
    return

def points():
    global A_points, B_points, C_points
    #todos cooperan
    if A == "C" and B == "C" and C =="C":
        A_points += 5
        B_points += 5
        C_points += 5
    #todos traicionan
    if A == "D" and B == "D" and C == "D":
        A_points += 2
        B_points += 2
        C_points += 2
    # dos cooperan
    if A == "C" and B == "C" and C == "D":
        A_points += 3
        B_points += 3
        C_points += 6
    if A == "C" and B == "D" and C == "C":
        A_points += 3
        B_points += 6
        C_points += 3
    if A == "D" and B == "C" and C == "C":
        A_points += 6
        B_points += 3
        C_points += 3
    # uno copera
    if A == "C" and B == "D" and C == "D":
        A_points += 0
        B_points += 4
        C_points += 4

    if A == "D" and B == "C" and C == "D":
        A_points += 4
        B_points += 0
        C_points += 4

    if A == "D" and B == "D" and C == "C":
        A_points += 4
        B_points += 4
        C_points += 0




numero_rondas = 100

for i in range(numero_rondas):

    # jugador A
    A = always_random()
    jugadas_A.append(A)

    # jugador B
    B = tit_for_tat_nervioso(i,"C")
    jugadas_B.append(B)

    # jugador C
    C = tit_for_tat_chill(i,"C")
    jugadas_C.append(C)

    # calcular puntos
    points()

    # guardar información de esta ronda
    history.append([i + 1, A, B, C, A_points, B_points, C_points])



print(history)


# Ruta donde está este script
folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "history.csv")


# Crear el archivo CSV
with open(file_path, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Cabecera
    writer.writerow(["Ronda", "A", "B","C", "Puntos A", "Puntos B", "Puntos C"])

    # Datos
    writer.writerows(history)


print(f"Archivo creado en: {file_path}")