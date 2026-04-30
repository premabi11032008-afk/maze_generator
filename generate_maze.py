import tkinter as tk
import random as rd
from a_star_algoritm import algo_a_star
from utils import get_available_direction,get_direction_dictionary

ROWS=10
walls=[[{"top":True,"bottom":True,"right":True,"left":True} for _ in range(ROWS)]for _ in range(ROWS)]

visited=set()
visited.add((0,0))

path=[(0,0)]
height=800//ROWS

MAZE_DONE=False

def grid_to_pixel(i, j):
    return (j * height + height // 2, i * height + height // 2)

def draw_square(x,y,canvas:tk.Canvas,color="green",
                border={"top":False,"bottom":False,"right":False,"left":False}):

    x1, y1 = x - (height // 2), y - (height // 2)
    x2, y2 = x + (height // 2), y + (height // 2)

    canvas.create_rectangle(x1, y1, x2, y2, fill=color,outline="")

    if border["top"]:
        canvas.create_line(x1, y1, x2, y1)

    if border["bottom"]:
        canvas.create_line(x1, y2, x2, y2)

    if border["left"]:
        canvas.create_line(x1, y1, x1, y2)

    if border["right"]:
        canvas.create_line(x2, y1, x2, y2)

def update_path():
    if not path:
        return

    last_i,last_j = path[-1]
    directions = get_available_direction(last_i,last_j,visited,ROWS)
    #print(path)

    if not directions:
        path.pop()
        #print(path)

        if not path:
            global MAZE_DONE
            MAZE_DONE = True
            run_astar_visual()
            return

        root.after(100, update_path)
        return

    dx,dy = rd.choice(directions)
    nx,ny = last_i+dx,last_j+dy

    visited.add((nx,ny))

    walls[last_i][last_j][get_direction_dictionary[(dx,dy)]] = False
    walls[nx][ny][get_direction_dictionary[(-dx,-dy)]] = False

    path.append((nx,ny))

    root.after(100, update_path)

def run_astar_visual():
    search_nodes, final_path = algo_a_star(walls, ROWS-1, ROWS-1,ROWS)
    animate_search(search_nodes, final_path)

def animate_search(search_nodes, final_path):
    index = 0

    def step():
        nonlocal index

        if index < len(search_nodes):
            i,j = search_nodes[index]
            x,y = grid_to_pixel(i,j)
            draw_square(x,y,canvas,"orange",walls[i][j])
            index += 1
            root.after(50, step)

        else:
            animate_path(final_path)

    step()

def animate_path(path):
    index = 0

    def step():
        nonlocal index

        if index < len(path):
            i,j = path[index]
            x,y = grid_to_pixel(i,j)
            draw_square(x,y,canvas,"blue",walls[i][j])
            index += 1
            root.after(100, step)

    step()

def update_canvas(canvas):
    if MAZE_DONE:
        return

    canvas.delete("all")

    for i in range(ROWS):
        for j in range(ROWS):
            if (i,j) in visited:
                x, y = grid_to_pixel(i, j)
                draw_square(x, y, canvas,"green",walls[i][j])

    root.after(100, lambda: update_canvas(canvas))

root=tk.Tk()
root.geometry("800x800")
root.title("Mace")

canvas=tk.Canvas(root)
canvas.pack(expand=True,fill="both")

update_canvas(canvas)
update_path()

root.mainloop()