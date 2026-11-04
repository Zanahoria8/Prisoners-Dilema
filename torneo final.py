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






def always_cooperate(estrat1,estrat2,estrat3):
    return "C"


def always_deflect(estrat1,estrat2,estrat3):
    return "D"

def always_random(historial_propio, historial_rival_1, historial_rival_2):
    return random.choice(["C", "D"])




def tolerante(historial_propio, historial_rival_1, historial_rival_2):
    if not historial_propio:
        return "C"

    if historial_rival_1[-1] == "D" and historial_rival_2[-1] == "D":
        return "D"

    return "C"


def estricto(historial_propio, historial_rival_1, historial_rival_2):
    if not historial_propio:
        return "C"

    if historial_rival_1[-1] == "C" and historial_rival_2[-1] == "C":
        return "C"

    return "D"





lista_estrats = [always_random,always_cooperate,always_deflect,tolerante,estricto]




def points(A,B,C):
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




def partida(estrat1,estrat2,estrat3):

    numero_rondas = 100

    for i in range(numero_rondas):

        # jugador A
        A = estrat1(jugadas_A,jugadas_C,jugadas_B)
        

        # jugador B
        B = estrat2(jugadas_B,jugadas_A,jugadas_C)
        

        # jugador C
        C = estrat3(jugadas_C,jugadas_A,jugadas_B)
        

        jugadas_A.append(A) # han de estar al final para que todas decidan a la vez
        jugadas_B.append(B)
        jugadas_C.append(C)
        # calcular puntos
        points(A,B,C)

        # guardar información de esta ronda
        history.append([
            estrat1.__name__,
            estrat2.__name__,
            estrat3.__name__,
            i + 1,
            A, B, C,
            A_points, B_points, C_points
        ])





    

print(history)

def guardar():
    # Ruta donde está este script
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, ""+"history.csv")

    # Crear el archivo CSV
    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        # Cabecera
        writer.writerow([
            "Estrategia A",
            "Estrategia B",
            "Estrategia C",
            "Ronda",
            "A", "B", "C",
            "Puntos A", "Puntos B", "Puntos C"
        ])

        # Datos
        writer.writerows(history)


    print(f"Archivo creado en: {file_path}")




### logica partidas

var1 = 0
var2 = 0
var3 = 0

for var1 in range(5):
    for var2 in range(5):
        for var3 in range(5):

            # Reiniciar historiales
            jugadas_A.clear()
            jugadas_B.clear()
            jugadas_C.clear()

            # Reiniciar puntos
            A_points = 0
            B_points = 0
            C_points = 0

            # Ejecutar partida
            partida(
                lista_estrats[var1],
                lista_estrats[var2],
                lista_estrats[var3]
            )


print("Partidas jugadas:", len(history) // 100)
print("Rondas totales:", len(history))
print("Última ronda:", history[-1])

guardar()
print("fin")
# bombo