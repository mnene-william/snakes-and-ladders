import tkinter as tk


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

ROWS = 10
COLUMNS = 10
SQUARE_BOX_SIZE = 70


def draw_game_board(canvas):
    for row in range(ROWS):
        for column in range(COLUMNS):
            color = "blue" if (row + column) % 2 == 0 else "orange"

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






def game_window():
    
    window = tk.Tk()
    window.title("Snakes and Ladders")

    window.geometry("700x700")
    window.resizable(False, False)

    game_board = tk.Canvas(window, width=700, height=700, bg="white")
    game_board.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
 
  
    draw_game_board(game_board)
    board_number()
    put_numbers_on_board(game_board)
    drawing_the_snakes_and_ladders(game_board)

    window.mainloop()

if __name__ == "__main__":
    game_window()