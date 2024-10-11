


def move_snake(app):
    app.head_pos = get_next_head_poistion(app.head_pos,app.direction)
    row,col = app.head_pos
    
    if is_legal(app.head_pos,app.board) == False:
        app.state = "gameover"
        write_to_csv("comp/scoreboard.csv",[navn,app.score]) if LOAD_BACKEND == True else  None
        sort_scoreboard("comp/scoreboard.csv") if LOAD_BACKEND == True else  None
        
        
    if app.state == "active":
        if app.board[row][col] == -1:
            app.snake_size += 1
            app.board[row][col] = app.snake_size
            apple_at_random_locatio(app.board)
            app.score += 1
        else:
            reset(app.board)
            app.board[row][col] = app.snake_size
    

def app_started(app):
    


   app.direction = "east"
   app.timer_delay = SPEED
   app.state = "start" # start, active, game_over
   app.info_mode = False
   app.score = 0 
   
   app.board = dynamic_board(HEIGHT,WIDTH,RUTER)
   

   app.snake_size = 3
   app.head_pos = (3, 4)

   
   
def timer_fired(app):
    if app.info_mode != True and app.state == "active":
        move_snake(app)

def key_pressed(app, event):
    global WIDTH
    global HEIGHT
    global SPEED
    global RUTER
    global DARKMODE
    global VANNSKELIGHETSGRAD
    
    if event.key == "D":
        if app.info_mode == True:
            app.info_mode = False
        else:
            app.info_mode = True 
    if app.info_mode == True:
        if event.key == "l":
            move_snake(app)
            
    

    # ting som alltid skal være på :)
    if event.key == "r":        
        app_started(app)
    if event.key == "q":
        exit()
        
    
    
        
    if event.key == "m":
        if DARKMODE == True:
            DARKMODE = False
        else:
            DARKMODE = True
    
    
    # start scree
    
    if app.state == "start":
        if event.key == "s":
            app.state = "active"
        if event.key == "1":
            VANNSKELIGHETSGRAD = 1
            SPEED = 250
            app_started(app)
        if event.key == "2":
            VANNSKELIGHETSGRAD = 2
            SPEED = 150
            app_started(app)
        if event.key == "3":
            VANNSKELIGHETSGRAD = 3
            SPEED = 75
            app_started(app)
            
            
    if event.key == "i" and app.state != "active":
        app.state = "info_screen" if app.state != "info_screen" else "start"
    if event.key == "o" and app.state != "active":
        app.state = "options" if app.state != "options" else "start"
            
    # må potesensielt endres senere
    if app.state == "active":
        if event.key == "w":
            app.direction = "north"
        if event.key == "s":
            app.direction = "south"
        if event.key == "a":
            app.direction = "west"
        if event.key == "d":
            app.direction = "east"
        
        
      

def redraw_all(app, canvas):
    draw_board(canvas, 25, 25, WIDTH-25, HEIGHT-25, app.board, app.info_mode, DARKMODE)
    
    if app.info_mode == True:
        canvas.create_text(WIDTH/2, 10, text=f"{app.head_pos=} {app.snake_size=} {app.direction=} {app.state=}")
    
    
    if app.state == 'active':
        pass
    elif app.state == "info_screen":
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 50, text="Press W to move up", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 125, text="Press S to move down", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 200, text="Press A to move left", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 275, text="Press D to move right", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 350, text="Press R to restart", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 425, text="Press Q to quit", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 500, text="Press M to toggle dark mode", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 575, text="Press I for info screen", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, 650, text="Press O for options", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))   
    elif app.state == "options":
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2)-150, text=f"Width: {WIDTH}\nHeight: {HEIGHT}\nSpeed: {SPEED}", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2)-50, text=f"Default White: {DATA['defult_white']}", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2), text=f"Default Black: {DATA['defult_black']}", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2)+100, text=f"Ruter: {RUTER}", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2)+150, text=f"Speed: {SPEED}", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2)+50, text=f"Dark Mode: {'On' if DARKMODE else 'Off'}", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))  
        canvas.create_text(WIDTH/2, (HEIGHT/2)+200, text=f"Du kan oppdatere innstilligne i parametre.json ", font=("Game over", 75), fill=font_mode_dark_mode(DARKMODE))
    elif app.state == "start":
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=dark_mode(DARKMODE))
        
        canvas.create_text(WIDTH/2, (HEIGHT/2)-220, text="Snake", font=("Game over", 300), fill="cyan")
        canvas.create_text(WIDTH/2, (HEIGHT/2)-100, text="Press S to start ", font=("Game over",200), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2), text="Press  I  for info", font=("Game over", 100), fill="red")
        canvas.create_text(WIDTH/2, (HEIGHT/2)+100, text="Press  O  for options", font=("Game over", 100), fill="red")
        canvas.create_text(WIDTH/2, (HEIGHT/2)+200, text="Press 1 for difficulty 1", font=("Game over", 50), fill="red")
        canvas.create_text(WIDTH/2, (HEIGHT/2)+250, text="Press 2 for difficulty 2", font=("Game over", 50), fill="red")
        canvas.create_text(WIDTH/2, (HEIGHT/2)+300, text="Press 3 for difficulty 3", font=("Game over", 50), fill="red")   
        canvas.create_text((WIDTH/2), (HEIGHT/2)+350, text=f"Difficulty: {VANNSKELIGHETSGRAD}", font=("Game over", 50), fill="cyan")

    elif app.state ==  "gameover":
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2)-200, text="Game Over", font=("Game over", 300), fill=font_mode_dark_mode(DARKMODE))
        canvas.create_text(WIDTH/2, (HEIGHT/2), text=f"Score: {app.score}", font=("Game over", 100), fill="cyan")
        canvas.create_text(WIDTH/2, (HEIGHT/2)+200, text="Press R to restart", font=("Game over", 100), fill="red")
        
       
       


if __name__ == '__main__':
    from uib_inf100_graphics.event_app import run_app
    from uib_inf100_graphics.helpers import load_image
    from funksjoner import *
    DATA = load_json("parametre.json")
    
    # backend
    LOAD_BACKEND = DATA["backend_load"]
   
    if LOAD_BACKEND == True:
        navn = input("Spillernavn?")
        
        
    
    
    WIDTH = DATA["width"]
    HEIGHT = DATA["height"]
    SPEED = DATA["speed"]
    DARKMODE = DATA["dark_mode"]
    RUTER = DATA["ruter"]
    VANNSKELIGHETSGRAD = DATA["difficulty"]

    run_app(width=WIDTH, height=HEIGHT, title='Snake')