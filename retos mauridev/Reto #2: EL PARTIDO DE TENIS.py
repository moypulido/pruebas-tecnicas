# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */

puntos = {
    0: "Love",
    1: "15",
    2: "30",
    3: "40"
}

def tennis_scoreboard(points):
    P1 = P2 = 0
    for point in points:
        if point == "P1":
            P1 += 1
        elif point == "P2":
            P2 += 1
        # Deuce
        if P1 >= 3 and P2 >= 3:
            if P1 == P2:
                print("Deuce")
            elif P1 == P2 + 1:
                print("Ventaja P1")
            elif P2 == P1 + 1:
                print("Ventaja P2")
            elif P1 >= P2 + 2:
                print("Ha ganado el P1")
                break
            elif P2 >= P1 + 2:
                print("Ha ganado el P2")
                break
        else:
            print(f"{puntos.get(P1, 'Error')} - {puntos.get(P2, 'Error')}")
            if P1 == 4:
                print("Ha ganado el P1")
                break
            if P2 == 4:
                print("Ha ganado el P2")
                break

tennis_scoreboard(["P2", "P1", "P2", "P2", "P1", "P2", "P2", "P1"])