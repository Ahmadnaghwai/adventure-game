# game_utils.py

def solve_riddle(riddle, answer):
    """Check if the player's answer to a riddle is correct."""
    return answer.lower() == riddle['answer'].lower()

def end_game(message):
    """Print a goodbye message and end the game."""
    print(message)
    exit()
