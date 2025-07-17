import random 
import time

SNAKES = {
    99: 80,
    95: 75,
    93: 73,
    89: 70,
    74: 53,
    64: 60,
    58: 23,
    49: 32,
    47: 26,
    16: 6
}

LADDERS = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

FINAL_POSITION = 100
START_POSITION = 0


def game_intro():
    print("Welcome to the snake and ladder game")
    print("Version 1.0")
    print("\n Game Rules")
    print("1. All players start at position 0")
    print("2. You should roll the dice in turns")
    print("3. Move foward the number of spaces shown on the dice.")
    print("4. If you land at the bottom of the ladder, you move up to the top of the ladder.")
    print("5. If you land at the head of a snake, you must slide down to the bottom of the snake.")
    print("6. Click ENTER to roll the dice.")
    print("7. The fisrt player to get to the FINAL(100) position is the winner.")

if __name__ == "__main__":
    game_intro()



