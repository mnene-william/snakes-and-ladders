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
    print("5. If you land at the head of a snake, you must slide down to the tail of the snake.")
    print("6. Click ENTER to roll the dice.")
    print("7. The first player to get to the FINAL(100) position is the winner.")


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

    number_of_players = 0
    while number_of_players <= 0:
        try:
            number_of_players =  int(input("Enter the number of players (1-4):"))
            if (0 <= number_of_players > 4 ):
                print("Please enter a number between 1 and 4.")
        except:
            print("Invalid input . Please enter a number.")

    players = {}

    for i in range(number_of_players):
        while True:
            player_name = input(f"Enter name for Player {i + 1}:").strip()
            if player_name:
                 if player_name in players:
                    print(f"This {player_name} is already taken. Please another name.")
                 else:
                    players[player_name] = START
                    print(f"{player_name} is at position {START}.")
                    break
            else:
                print(f"Player name cannot be left empty. Please enter a name to play.")
    
    turn_order = list(players.keys())
    current_player_index = 0

    game_over = False
    print("The game is now starting")
    time.sleep(2)
   
    while not game_over:
        player_name = turn_order[current_player_index]
        current_position = players[player_name]

        print(f"It is {player_name}'s turn to play")
        print(f"Your current position: {current_position}")
        input("Press ENTER to roll the dice...")             

        roll = dice_roll()
        print(f"{player_name} rolled a {roll}!")

        position_after_roll = current_position + roll

        if position_after_roll > END:
            print("{player_name} will remain in the same position")
        else:
            print(f"{player_name} moving to position {position_after_roll}")
            time.sleep(1)
        
            final_position = check_position(player_name, position_after_roll) 
            players[player_name] = final_position

            print(f"{player_name}'s new position is {players[player_name]}")

            if players[player_name] == END:
               print(f"BRAVO, {player_name}! You have won the game! You are the first player to reach position {END}")
               game_over = True

        if not game_over:
            current_player_index = (current_player_index + 1) % number_of_players
            time.sleep(1)



       

    



if __name__ == "__main__":
    play_game()





