# # /*
# #  * Crea un programa que simule el comportamiento del sombrero seleccionador del
# #  * universo mágico de Harry Potter.
# #  * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# #  * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# #  * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
# #  *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# #  * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
# #  *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
# #  */

# houses = {
#     1 : "Gryffindor",
#     2 : "Ravenclaw",
#     3 : "Hufflepuff",
#     4 : "Slytherin",
# }

# def questions():

#     print("introduce el numero de tu respuesa \n")

#     answers = []
#     answers.append(int(input("""¿Qué valor consideras más importante?
#     1) Valentía
#     2) Inteligencia
#     3) Lealtad
#     4) Ambición
#     respuesta: """)))
#     answers.append(int(input("""¿Cuál de estas actividades prefieres?
#     1) Aventurarte en lo desconocido
#     2) Resolver acertijos difíciles
#     3) Ayudar a tus amigos
#     4) Liderar un grupo
#     respuesta: """)))
#     answers.append(int(input("""¿Qué animal te representa mejor?
#     1) León
#     2) Águila
#     3) Tejón
#     4) Serpiente
#     respuesta: """)))
#     answers.append(int(input("""¿Cómo enfrentas los problemas?
#     1) Con coraje
#     2) Analizando todas las opciones
#     3) Buscando apoyo en los demás
#     4) Aprovechando la oportunidad para destacar
#     respuesta: """)))
#     answers.append(int(input("""¿Qué cualidad valoras más en tus amigos?
#     1) Determinación
#     2) Sabiduría
#     3) Fidelidad
#     4) Ambición
#     respuesta: """)))

#     res = [0, 0, 0, 0]  # One score per house
#     for answer in answers:
#         if 1 <= answer <= 4:
#             res[answer-1] += 1  # Increment the score for the selected house

#     print("Puntajes por casa:", res)
#     print("¡Has sido seleccionado para la casa:", houses[res.index(max(res)) + 1] + "!")

# questions()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sombrero Seleccionador de Hogwarts (CLI)
- 5 preguntas mínimas, 4 opciones cada una.
- Puntúa por rasgos: Gryffindor (valentía), Ravenclaw (inteligencia),
  Hufflepuff (lealtad/trabajo duro), Slytherin (ambición/astucia).
- Valida entrada, maneja empates con desempate.
"""

from collections import defaultdict
import hashlib

HOUSES = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

TRAITS = {
    "Gryffindor": "valentía, audacia, determinación",
    "Ravenclaw":  "inteligencia, ingenio, creatividad",
    "Hufflepuff": "lealtad, constancia, justicia",
    "Slytherin":  "ambición, astucia, liderazgo"
}

# Cada pregunta mapea opciones a incrementos de puntuación por casa
QUESTIONS = [
    {
        "q": "¿Qué valor consideras más importante?",
        "opts": {
            "a": ("Valentía",      {"Gryffindor": 2}),
            "b": ("Inteligencia",  {"Ravenclaw": 2}),
            "c": ("Lealtad",       {"Hufflepuff": 2}),
            "d": ("Ambición",      {"Slytherin": 2}),
        }
    },
    {
        "q": "¿Cuál de estas actividades prefieres?",
        "opts": {
            "a": ("Aventurarte en lo desconocido", {"Gryffindor": 2, "Slytherin": 1}),
            "b": ("Resolver acertijos difíciles",   {"Ravenclaw": 2}),
            "c": ("Ayudar a tus amigos",            {"Hufflepuff": 2}),
            "d": ("Liderar un grupo",               {"Slytherin": 2, "Gryffindor": 1}),
        }
    },
    {
        "q": "¿Qué animal te representa mejor?",
        "opts": {
            "a": ("León",      {"Gryffindor": 2}),
            "b": ("Águila",    {"Ravenclaw": 2}),
            "c": ("Tejón",     {"Hufflepuff": 2}),
            "d": ("Serpiente", {"Slytherin": 2}),
        }
    },
    {
        "q": "¿Cómo enfrentas los problemas?",
        "opts": {
            "a": ("Con coraje inmediato",               {"Gryffindor": 2}),
            "b": ("Analizando todas las opciones",      {"Ravenclaw": 2}),
            "c": ("Buscando apoyo en los demás",        {"Hufflepuff": 2}),
            "d": ("Aprovechando para destacar/negociar",{"Slytherin": 2}),
        }
    },
    {
        "q": "¿Qué cualidad valoras más en tus amigos?",
        "opts": {
            "a": ("Determinación", {"Gryffindor": 2}),
            "b": ("Sabiduría",     {"Ravenclaw": 2}),
            "c": ("Fidelidad",     {"Hufflepuff": 2}),
            "d": ("Ambición",      {"Slytherin": 2}),
        }
    },
    # Preguntas extra (suman matices, por si quieres ampliar)
    {
        "q": "En un proyecto con fecha límite cercana, ¿qué haces primero?",
        "opts": {
            "a": ("Tomo riesgos calculados y empujo fuerte", {"Gryffindor": 2, "Slytherin": 1}),
            "b": ("Planifico con un diagrama y priorizo",    {"Ravenclaw": 2}),
            "c": ("Organizo al equipo y reparto tareas",     {"Hufflepuff": 2}),
            "d": ("Negocio recursos y visibilidad",          {"Slytherin": 2}),
        }
    },
]

# Pregunta de desempate (elige entre rasgos opuestos)
TIE_BREAKER = {
    "q": "Desempate: ¿qué te describe mejor ahora mismo?",
    "opts": {
        "a": ("Busco justicia y cuidar al equipo",    {"Hufflepuff": 2}),
        "b": ("Busco destacar y alcanzar la cima",    {"Slytherin": 2}),
        "c": ("Busco conocimiento y resolver misterios", {"Ravenclaw": 2}),
        "d": ("Busco acción y defender lo correcto",  {"Gryffindor": 2}),
    }
}

def ask(question_block):
    print("\n" + question_block["q"])
    for key, (label, _) in question_block["opts"].items():
        print(f"  {key}) {label}")
    while True:
        choice = input("Elige (a/b/c/d): ").strip().lower()
        if choice in question_block["opts"]:
            return choice
        print("Entrada no válida. Por favor escribe a, b, c o d.")

def apply_scores(scores, question_block, choice):
    _, deltas = question_block["opts"][choice]
    for house, inc in deltas.items():
        scores[house] += inc

def top_houses(scores):
    max_score = max(scores.values())
    return [h for h, s in scores.items() if s == max_score], max_score

def stable_choice_from_name(name, candidates):
    # Semilla reproducible: hash del nombre → índice
    h = hashlib.sha256(name.encode("utf-8")).hexdigest()
    idx = int(h, 16) % len(candidates)
    return candidates[idx]

def main():
    print("🧙 Sombrero Seleccionador de Hogwarts")
    print("-------------------------------------")
    name = input("Tu nombre (para desempates reproducibles): ").strip() or "Muggle"

    scores = defaultdict(int)
    # Usa las primeras 5 preguntas; puedes ampliar a más si quieres
    for i, qb in enumerate(QUESTIONS[:5], 1):
        choice = ask(qb)
        apply_scores(scores, qb, choice)

    # Resultado inicial
    candidates, max_score = top_houses(scores)

    # Desempate si es necesario
    if len(candidates) > 1:
        print("\n🏁 Tenemos un empate entre:", ", ".join(candidates))
        choice = ask(TIE_BREAKER)
        apply_scores(scores, TIE_BREAKER, choice)
        candidates, max_score = top_houses(scores)

        # Si aún hay empate, elige estable por nombre
        if len(candidates) > 1:
            chosen = stable_choice_from_name(name, candidates)
        else:
            chosen = candidates[0]
    else:
        chosen = candidates[0]

    print("\n🎩 ¡El Sombrero ha decidido!")
    print(f"➡️  {name}, tu casa es: \033[1m{chosen}\033[0m")
    print(f"   Rasgos: {TRAITS[chosen]}")
    print("\nPuntuaciones finales:")
    for h in HOUSES:
        print(f"  {h}: {scores[h]}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelado por el usuario. ¡Hasta la próxima!")
