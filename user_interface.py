import tkinter as tk
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
FIRST_SQUARE = 1

ROWS = 10
COLUMNS = 10
SQUARE_BOX_SIZE = 70

PLAYER_TOKEN_COLORS = ["#ff0000", "#0000ff", "#ffff00", "#800080"]


def draw_game_board(canvas):
    for row in range(ROWS):
        for column in range(COLUMNS):
             
            if (row + column) % 2 == 0:
                color = "blue"
            else:
                color = "orange"

            x1 = column * SQUARE_BOX_SIZE
            y1 = row * SQUARE_BOX_SIZE
            x2 = x1 + SQUARE_BOX_SIZE
            y2 = y1 + SQUARE_BOX_SIZE


            canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=1)

BOARD_UNITS= {}

def drawing_the_snakes_and_ladders(canvas):
    for start_position, end_position in LADDERS.items():
        x1, y1 = BOARD_UNITS[start_position]
        x2, y2 = BOARD_UNITS[end_position]

        ladder_color = "#895129"

        canvas.create_line(x1, y1, x2, y2, fill=ladder_color, width=4, capstyle=tk.ROUND)


        canvas.create_oval(x1-3, y1-3, x1+3, y1+3, fill=ladder_color)
        canvas.create_oval(x2-3, y2-3, x2+3, y2+3, fill=ladder_color)

    for start_position, end_position in SNAKES.items():
        x1, y1 = BOARD_UNITS[start_position]
        x2, y2 = BOARD_UNITS[end_position]

        snakes_color = "#008000"

        canvas.create_line(x1, y1, x2, y2, fill=snakes_color, width=4, capstyle=tk.ROUND)
        canvas.create_oval(x1-3, y1-3, x1+3, y1+3, fill=snakes_color)
        canvas.create_oval(x2-3, y2-3, x2+3, y2+3, fill=snakes_color)


def board_number():
    for number in range(1, END + 1):
        actual_row = (number - 1) // COLUMNS

        if actual_row % 2 == 0:
            actual_column = (number -1) % COLUMNS
        else:
            actual_column = COLUMNS - 1 -((number - 1) % COLUMNS)

        first_row = (ROWS - 1) - actual_row

        x_top_cordinate = actual_column * SQUARE_BOX_SIZE
        y_top_cordinate = first_row * SQUARE_BOX_SIZE

        x_center_cordinate = (SQUARE_BOX_SIZE * 0.5)  + x_top_cordinate
        y_center_cordinate = (SQUARE_BOX_SIZE * 0.5) + y_top_cordinate

        BOARD_UNITS[number] = (x_center_cordinate, y_center_cordinate)


def put_numbers_on_board(canvas):
    for pos in range(1, END + 1):
        x_cordinate, y_cordinate = BOARD_UNITS[pos]
        canvas.create_text(x_cordinate, y_cordinate, text=str(pos), fill="black", font=("bold", 12))


class GameLogic:
    def __init__(self, master):
        self.master = master

        self.master.title("Snakes and Ladders")
        self.master.geometry("950x700")
        self.master.resizable(False, False)

        self.players_info = [
            {'name': 'Player 1', 'position': START, 'color': PLAYER_TOKEN_COLORS[0], 'id': None},
            {'name': 'Player 2', 'position': START, 'color': PLAYER_TOKEN_COLORS[1], 'id': None}

        ]
        
        self.num_players = len(self.players_info)
        self.player_index = 0

        self.game_board_frame = tk.Frame(self.master)
        self.game_board_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.game_controls = tk.Frame(self.master, width=250, bg="lightgray")
        self.game_controls.pack(side=tk.RIGHT, fill=tk.Y)
        self.game_controls.pack_propagate(False)

        self.game_board = tk.Canvas(self.game_board_frame, width=700, height=700, bg="white")
        self.game_board.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        draw_game_board(self.game_board)
        board_number()
        put_numbers_on_board(self.game_board)
        drawing_the_snakes_and_ladders(self.game_board)

        self.game_ui()


    def game_ui(self):

        for widget in self.game_controls.winfo_children():
            widget.destroy()


        self.current_player_lbl = tk.Label(
            self.game_controls, text="Current Turn:\n", bg="lightgray",
            font=("Poppins", 14, "bold")
        )
        self.current_player_lbl.pack(pady=10)

        self.dice_result_lbl = tk.Label(
            self.game_controls, text="Roll: -", bg="lightgray",font=("Poppins", 18, "bold") )
        self.dice_result_lbl.pack(pady=10)


        self.roll_button = tk.Button(
            self.game_controls, text="Roll Dice", command=self.roll_dice,font=("Poppins", 16, "bold") )
        self.roll_button.pack(pady=20)
        

        self.player_tokens()
        self.current_player()




    def get_player_position(self, player_info):

        logical_position = player_info['position']

        actual_square = FIRST_SQUARE if logical_position == START else logical_position
        

        x_cordinate_center_square, y_cordinate_center_square = BOARD_UNITS[actual_square]

       
        players_current_square = [player for player in self.players_info if (player['position'] == logical_position)]


        num_players_current_square = len(players_current_square)
        
        
        current_player_in_group_index = 0

        for index, player in enumerate(players_current_square):

            if player == player_info:
                current_player_in_group_index = index
                break


        spacing = 15 * 2 + 5 
        total_width_occupied = (num_players_current_square - 1) * spacing
        

        start_x_offset = x_cordinate_center_square - (total_width_occupied * 0.5)
        
        final_x = start_x_offset + (current_player_in_group_index * spacing)
        final_y = y_cordinate_center_square 

        return final_x, final_y

    def player_tokens(self):
        for player in self.players_info:
            if player['id']:
                self.game_board.delete(player['id'])

            x_cord, y_cord = self.get_player_position(player)

            id = self.game_board.create_oval(
                x_cord - 15, y_cord - 15,
                x_cord + 15, y_cord + 15, width=1, outline="black", fill=player['color'])
            
            player['id'] = id

    def current_player(self):
        current_player = self.players_info[self.player_index]
        self.current_player_lbl.config(text=f"It is {current_player['name']}'s turn", fg="black")

    def move_player_token(self, player, new_position):

        player['position'] = new_position

        self.player_tokens()


    def check_for_snake_ladder(self, player_position):

        if player_position in LADDERS:
            print(f" Bravo! Landed on a ladder from {player_position} to {LADDERS[player_position]}")
            return LADDERS[player_position]

        elif player_position in SNAKES:
            print(f" Oh no! Landed on a snake from {player_position} to {SNAKES[player_position]}")
            return SNAKES[player_position]
        return player_position


    def roll_dice(self):
        current_player = self.players_info[self.player_index]
        roll = random.randint(1, 6)
        self.dice_result_lbl.config(text=f"Roll: {roll}")
        print(f"{current_player['name']} rolled a {roll}")


        new_position = current_player['position'] + roll


        if new_position > END:
            new_position = END
        

        self.move_player_token(current_player, new_position)
        print(f"The {current_player['name']} has moved to {new_position}")


        if new_position == END:
            self.roll_button.config(state=tk.DISABLED) 
            self.current_player_lbl.config(text=f"GAME OVER! The {current_player['name']} Wins this round!", fg="green")
            print(f"CONGRATULATIONS,{current_player['name']}! You have won the game! ")
            return 

 
        final_position_after_jump = self.check_for_snake_ladder(new_position)
        if final_position_after_jump != new_position:

            self.move_player_token(current_player, final_position_after_jump)
            print(f"The {current_player['name']} moved to {final_position_after_jump}")


        self.player_index = (self.player_index + 1) % self.num_players
        self.current_player()



def game_window():
    window = tk.Tk()
    game = GameLogic(window) 
    window.mainloop()

if __name__ == "__main__":
    game_window()
                


            
            

        



        





        
        





    










def game_window():
    
    window = tk.Tk()

    window.mainloop()

if __name__ == "__main__":
    game_window()