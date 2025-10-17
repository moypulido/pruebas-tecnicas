#Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# La función recibe un listado que contiene pares, representando cada jugada.
# El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
# "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# Debes buscar información sobre cómo se juega con estas 5 posibilidades.
# */

def rpsls_game(plays):
    rules = {
        "🗿": ["✂️", "🦎"],
        "📄": ["🗿", "🖖"],
        "✂️": ["📄", "🦎"],  
        "🦎": ["📄", "🖖"],   
        "🖖": ["🗿", "✂️"]
    }

    score = {"Player 1": 0, "Player 2": 0}

    for play in plays:
        p1, p2 = play
        if p1 == p2:
            continue
        elif p2 in rules[p1]:
            score["Player 1"] += 1
        else:
            score["Player 2"] += 1

    if score["Player 1"] > score["Player 2"]:
        return "Player 1"
    elif score["Player 2"] > score["Player 1"]:
        return "Player 2"
    else:
        return "Tie"


# Ejemplo de uso
plays = [("🗿", "✂️"), ("✂️", "🥄"), ("🦎", "🥄")]

result = rpsls_game(plays)
print(result)