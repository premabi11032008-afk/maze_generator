import tkinter as tk
from a_star_algoritm import algo_a_star
from utils import grid_to_pixel,draw_square
from generate_maze_dfs import generate_maze_dfs
from generate_maze_prisms import generate_maze_prisms

def animate_search(search_nodes, final_path , height):
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
            animate_path(final_path , height)

    step()

def animate_path(path , height):
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

def run_visualization(generator_fn, solver_fn , canvas, height):
    generator = generator_fn(walls, ROWS)

    def step_generation():
        try:
            visited , walls = next(generator)
            update_canvas(canvas,visited , walls , height)

            root.after(50, step_generation)

        except StopIteration:
            run_solver()

    def run_solver():
        search_nodes, final_path = solver_fn(walls, ROWS-1, ROWS-1, ROWS)
        animate_search(search_nodes, final_path,height)

    step_generation()


def update_canvas(canvas, visited , walls, height):

    canvas.delete("all")

    for i in range(ROWS):
        for j in range(ROWS):
            if (i,j) in visited:
                x, y = grid_to_pixel(i, j , height)
                draw_square(x, y, canvas, height ,"green",walls[i][j])

root=tk.Tk()
root.geometry("800x800")
root.title("Mace")

ROWS=30
walls=[[{"top":True,"bottom":True,"right":True,"left":True} for _ in range(ROWS)]for _ in range(ROWS)]
height=800//ROWS

canvas=tk.Canvas(root)
canvas.pack(expand=True,fill="both")

run_visualization(generate_maze_dfs,algo_a_star,canvas ,height)

root.mainloop()