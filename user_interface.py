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

ROWS = 10
COLUMNS = 10
SQUARE_BOX_SIZE = 50

WIDTH = ROWS * SQUARE_BOX_SIZE
HEIGHT = COLUMNS * SQUARE_BOX_SIZE

def game_window():
    
    window = tk.Tk()