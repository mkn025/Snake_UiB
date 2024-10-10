from json import load 
from random import randint
import csv


def write_to_csv(file_path, row):
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)
    


def sort_scoreboard(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        sortedlist = sorted(reader, key=lambda row: int(row['score']), reverse=True)
        
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in sortedlist:
            writer.writerow(row)



def load_json(file_path):
    with open(file_path, 'r') as file:
        return load(file)
    

DATA = load_json("parametre.json")
    
DEFULT_WHITE = DATA["defult_white"]
DEFULT_BLACK = DATA["defult_black"]
SNAKE_COLOR = DATA["snake_color"]
FOOD_COLOR = DATA["food_color"]
#hjelpefunksjoner



def dark_mode(mode:bool,color_white=DEFULT_WHITE,color_black=DEFULT_BLACK):
    if mode == False:
        return color_white
    else:
        return color_black # fake black
    
def font_mode_dark_mode(mode:bool,color_white=DEFULT_WHITE,color_black=DEFULT_BLACK):
    if mode == False:
        return color_black # 
    else:
        return color_white

def is_legal(pos,board):
    if pos[0] >= len(board):
        return False
    if pos[0] < 0:
        return False
    if pos[1] >= len(board[0]):
        return False
    if pos[1] < 0:
        return False
    # kræsj med seg selv :=)
    if board[pos[0]][pos[1]] > 0:
        return False

    return True



def get_next_head_poistion(head,direction):
    row,col = head
    if direction == "north":
        return(row-1,col)
    if direction == "south":
        return (row + 1, col)
    elif direction == "west":
        return (row, col - 1)
    elif direction == "east":
        return (row, col + 1)
    

def reset(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] > 0:
                board[row][col] -= 1
                

def pick_random_kods(x,y):     
    return (randint(1,x-1),randint(1,y-1))

def apple_at_random_locatio(board:list):
    row = len(board)
    col = len(board[0])
   

    random_row = pick_random_kods(row,col)[0]
    random_col = pick_random_kods(row,col)[1]

    while True:
        if board[random_row][random_col] > 1:
            random_row = pick_random_kods(row,col)[0]
            random_col = pick_random_kods(row,col)[1]
        else:
            board[random_row][random_col] = -1
            break


def get_color(value, color:bool):
    if value == 0:
        return dark_mode(color,"lightgray")
    elif value > 0:
        return SNAKE_COLOR
    else:
        return FOOD_COLOR   
    
    
def draw_board(canvas, x1, y1, x2, y2, board, info_mode:bool, dark_mode:bool):
    rows = len(board)
    cols = len(board[0])

    cell_width = (x2 - x1) / cols
    cell_height = (y2 - y1) / rows

    for row in range(rows):
        for col in range(cols):

      
            cell_left = x1 + col * cell_width
            cell_top = y1 + row * cell_height
            cell_right = cell_left + cell_width
            cell_bottom = cell_top + cell_height
            color = get_color(board[row][col],dark_mode)
            
            
            canvas.create_rectangle(
                cell_left, cell_top, cell_right, cell_bottom,
                fill=color
            )
            
            if info_mode == True:
                canvas.create_text(cell_left + cell_width/2, cell_top + cell_height/2, text=f"{row},{col}\n {board[row][col]}", fill=font_mode_dark_mode(dark_mode))
            else:
                pass
            


def dynamic_board(width, height,ruter):
    board = []
    for _ in range(height // ruter):
        board.append([0] * (width // ruter))
    
    # Set start position at (3, 4) with length 3
    start_pos = (3, 4)
    length = 3
    for i in range(length):
        board[start_pos[0]][start_pos[1] - i] = length - i

    # Add apple at a random location
    apple_at_random_locatio(board)
    return board




