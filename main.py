# main.py
import random
from game_utils import solve_riddle, end_game

def greeting():
    """Greet the player and explain the rules."""
    print("Willkommen zu 'Die verlorene Schatzsuche'!")
    print("Du wirst durch verschiedene Räume navigieren und Rätsel lösen.")
    print("Das Ziel ist es, den Schatz zu finden. Viel Glück!\n")

def enter_room(room):
    """Describe the current room and available actions."""
    print(room['description'])
    if 'riddle' in room:
        print(f"Hier ist ein Rätsel: {room['riddle']['text']}")
        answer = input("Was ist deine Antwort? ")
        if solve_riddle(room['riddle'], answer):
            print("Rätsel gelöst! Du darfst weiter.")
            return True
        else:
            print("Das war falsch. Versuche es noch einmal.")
            return False
    return True

def main():
    """Main game function."""
    greeting()

    rooms = {
        'start': {
            'description': "Du bist im Startzimmer. Es gibt einen Ausgang nach Norden.",
            'riddle': {
                'text': "Was hat vier Beine am Morgen, zwei Beine am Mittag und drei Beine am Abend?",
                'answer': "Der Mensch"
            }
        },
        'treasure_room': {
            'description': "Du bist im Schatzraum! Herzlichen Glückwunsch, du hast den Schatz gefunden!",
            'riddle': None
        },
        'second_room': {
            'description': "Du bist im zweiten Raum. Hier gibt es eine Tür nach Süden.",
            'riddle': {
                'text': "Ich spreche ohne Mund und höre ohne Ohren. Ich habe keinen Körper, aber ich komme am Leben. Was bin ich?",
                'answer': "Echo"
            }
        }
    }

    current_room = 'start'

    while True:
        if enter_room(rooms[current_room]):
            if current_room == 'start':
                current_room = 'second_room'
            elif current_room == 'second_room':
                current_room = 'treasure_room'
            elif current_room == 'treasure_room':
                end_game("Danke, dass du gespielt hast! Bis zum nächsten Mal!")

if __name__ == "__main__":
    main()
