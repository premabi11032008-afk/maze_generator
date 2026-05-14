import tkinter as tk
from generate_maze_prisms import generate_maze_prisms
from utils import grid_to_pixel,draw_square,get_final_walls,get_direction_dictionary
from animate_maze import run_solver
from queue_algorithm import queue_algorithm

def draw_player(i,j,height,canvas):
    x,y=grid_to_pixel(i,j,height)
    canvas.create_oval(x-height//2,y-height//2,x+height//2,y+height//2,fill="red")

def update_game(canvas,maze,height):
    canvas.delete("all")

    for i in range(ROWS):
        for j in range(ROWS):
            x,y=grid_to_pixel(i,j,height)
            draw_square(x,y,canvas,height,"grey",maze[i][j])
    
    draw_player(*player_pos,height,canvas)
    root.after(50,lambda : update_game(canvas,maze,height))

def handle_key_press(event):
    pressed_keys.add(event.keysym)

def handle_key_release(event):
    game_loop()
    pressed_keys.discard(event.keysym)
    

def game_loop():
    global player_pos

    x, y = player_pos
    dx,dy=0,0

    if "Up" in pressed_keys:
        dx -= 1
    if "Down" in pressed_keys:
        dx += 1
    if "Left" in pressed_keys:
        dy -= 1
    if "Right" in pressed_keys:
        dy += 1

    nx,ny=x+dx,y+dy
    if nx>=ROWS or nx<0 or ny>=ROWS or ny<0 or ( (dx,dy) in get_direction_dictionary and walls[x][y][get_direction_dictionary[(dx,dy)]]==True):
        player_pos=(x,y)
    else:
        player_pos=(nx,ny)

root=tk.Tk()
root.geometry("1000x1600")
root.title("Mace Game")

canvas_size=800
frame_size_x=800
frame_size_y=800
player_pos=0,0
pressed_keys=set()

ROWS=20

walls=[[{"top":True,"bottom":True,"right":True,"left":True} for _ in range(ROWS)]for _ in range(ROWS)]
height=(canvas_size)/ROWS

frame = tk.Frame(root, height=frame_size_x,width=frame_size_y)
frame.pack_propagate(False)
frame.pack()

canvas = tk.Canvas(frame, width=canvas_size, height=canvas_size)
canvas.grid(row=0, column=0)

maze=get_final_walls(generate_maze_prisms,walls,ROWS)

game_loop()
update_game(canvas,maze,height)
run_solver(queue_algorithm,maze,canvas,ROWS,height,root)

root.bind("<KeyPress>", handle_key_press)
root.bind("<KeyRelease>", handle_key_release)

root.mainloop()