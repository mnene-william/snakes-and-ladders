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
START = 0
END = 100



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


def dice_roll():
    return random.randint(1, 6)

def check_position(player_name, position):

    if position in SNAKES:
        new_position = SNAKES[position]
        print(f"\n Oh no! {player_name} landed on a snake head at {position}! Sliding down to {new_position}...")
        return new_position
    
    elif position in LADDERS:
        new_position = LADDERS[position]
        print(f"Way to go {player_name}! You found a ladder at position {position}! Climbing to {new_position}..")
        return new_position
    else:
        return position 
    
def play_game():
    game_intro()

    num_players = 0
    while not (1 <= num_players <= 4):
        try:
            num_players =  int(input("Enter the number of players (1-4):"))
            if not (1 <= num_players <= 4):
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input . Please enter a number.")

    players = {}

    for i in range(num_players):
        while True:
            player_name = input(f"Enter name for Player {i + 1}:").strip()
            if player_name:
                 if player_name in players:
                    print(f"{player_name} is already taken. Please enter a unique name.")
                 else:
                    players[player_name] = START
                    print(f"{player_name} starts at position {START}.")
                    break
            else:
                print(f"Player name cannot be empty. Please enter a name.")
    
    turn_order = list(players.keys())
    current_player_index = 0


    



if __name__ == "__main__":
    game_intro()
    
    print("Rolling the dice 5 times:")
    for i in range(5):
        roll_result = dice_roll()
        print(f"Roll {i+1}: {roll_result}")
        time.sleep(0.5)

        test_player = "Test Player"

        test_pos_ladder = 21
        print(f"\n{test_player} is at {test_pos_ladder}. Checking for ladder...")
        updated_pos_ladder = check_position(test_player, test_pos_ladder)
        print(f"New position after check: {updated_pos_ladder}")
        time.sleep(1)

        test_pos_snake = 99
        print(f"\n{test_player} is at {test_pos_snake}. Checking for snake...")
        updated_pos_snake = check_position(test_player, test_pos_snake)
        print(f"New position after check:{updated_pos_snake}")
        time.sleep(1)

        test_pos_normal = 50
        print(f"\n{test_player} is at {test_pos_normal}. Checking for special square...")
        updated_pos_normal = check_position(test_player, test_pos_normal)
        print(f"New position after check: {updated_pos_normal}")
        time.sleep(1)





