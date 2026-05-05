import tkinter as tk
from a_star_algoritm import algo_a_star
from utils import grid_to_pixel,draw_square
from generate_maze_dfs import generate_maze_dfs
from generate_maze_prisms import generate_maze_prisms
from queue_algorithm import queue_algorithm
import copy

def animate_search(search_nodes, final_path , height , canvas , walls):
    index = 0

    def step():
        nonlocal index

        if index < len(search_nodes):
            i,j = search_nodes[index]
            x,y = grid_to_pixel(i,j ,height)
            draw_square(x,y,canvas,height,"orange",walls[i][j])
            index += 1
            root.after(50, step)

        else:
            animate_path(final_path , height , canvas, walls)

    step()

def animate_path(path , height , canvas , walls):
    index = 0

    def step():
        nonlocal index

        if index < len(path):
            i,j = path[index]
            x,y = grid_to_pixel(i,j , height)
            draw_square(x,y,canvas,height,"blue",walls[i][j])
            index += 1
            root.after(100, step)

    step()

def run_visualization(generator_fn, solver_fn , canvas, height , walls):
    generator = generator_fn(walls, ROWS)

    def step_generation():
        try:
            visited , new_walls = next(generator)
            walls[:]=new_walls

            update_canvas(canvas,visited , walls , height)

            root.after(50, step_generation)

        except StopIteration:
            run_solver()

    def run_solver():
        search_nodes, final_path = solver_fn(walls, ROWS-1, ROWS-1, ROWS)
        animate_search(search_nodes, final_path,height , canvas , walls)

    step_generation()


def update_canvas(canvas, visited , walls, height):

    canvas.delete("all")

    for i in range(ROWS):
        for j in range(ROWS):
            if (i,j) in visited:
                x, y = grid_to_pixel(i, j , height)
                draw_square(x, y, canvas, height ,"green",walls[i][j])

root=tk.Tk()
root.geometry("1000x1600")
root.title("Mace")

ROWS=5

walls=[[{"top":True,"bottom":True,"right":True,"left":True} for _ in range(ROWS)]for _ in range(ROWS)]
height=(400)/ROWS

frame = tk.Frame(root, height=400,width=800)
frame.pack_propagate(False)
frame.pack()

canvas = tk.Canvas(frame, width=400, height=400)
canvas.grid(row=0, column=0)

canvas_2 = tk.Canvas(frame, width=400, height=400)
canvas_2.grid(row=0, column=1)

canvas_3 = tk.Canvas(frame, width=400, height=400)
canvas_3.grid(row=1, column=0)

canvas_4 = tk.Canvas(frame, width=400, height=400)
canvas_4.grid(row=1, column=1)

walls_2=copy.deepcopy(walls)
walls_3=copy.deepcopy(walls)
walls_4=copy.deepcopy(walls)

run_visualization(generate_maze_prisms,queue_algorithm, canvas ,height, walls)
run_visualization(generate_maze_prisms,algo_a_star, canvas_2 ,height , walls_2)
run_visualization(generate_maze_dfs,queue_algorithm, canvas_3,height, walls_3)
run_visualization(generate_maze_dfs,algo_a_star, canvas_4 ,height , walls_4)

root.mainloop()