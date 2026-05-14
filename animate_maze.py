import tkinter as tk
from a_star_algoritm import algo_a_star
from utils import grid_to_pixel,draw_square
from generate_maze_dfs import generate_maze_dfs
from generate_maze_prisms import generate_maze_prisms
from queue_algorithm import queue_algorithm

def animate_search(search_nodes, final_path , height , canvas , walls,root):
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
            animate_path(final_path , height , canvas, walls,root)

    step()

def animate_path(path , height , canvas , walls,root):
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

def run_visualization(generator_fn, solver_fn , canvas, height , walls,root):
    generator = generator_fn(walls, ROWS)

    def step_generation():
        try:
            visited , new_walls = next(generator)
            walls[:]=new_walls

            update_canvas(canvas,visited , walls , height)

            root.after(1, step_generation)

        except StopIteration:
            run_solver(solver_fn,walls,canvas,ROWS,height,root)

    step_generation()

def run_solver(solver_fn,walls,canvas,ROWS,height,root):
    search_nodes, final_path = solver_fn(walls, ROWS-1, ROWS-1, ROWS)
    animate_search(search_nodes, final_path,height , canvas , walls,root)

def update_canvas(canvas, visited , walls, height):

    canvas.delete("all")

    for i in range(ROWS):
        for j in range(ROWS):
            if (i,j) in visited:
                x, y = grid_to_pixel(i, j , height)
                draw_square(x, y, canvas, height ,"green",walls[i][j])

if __name__=="__main__":
    root=tk.Tk()
    root.geometry("1000x1600")
    root.title("Mace")

    canvas_size=800
    frame_size_x=800
    frame_size_y=800

    ROWS=20

    walls=[[{"top":True,"bottom":True,"right":True,"left":True} for _ in range(ROWS)]for _ in range(ROWS)]
    height=(canvas_size)/ROWS

    frame = tk.Frame(root, height=frame_size_x,width=frame_size_y)
    frame.pack_propagate(False)
    frame.pack()

    canvas = tk.Canvas(frame, width=canvas_size, height=canvas_size)
    canvas.grid(row=0, column=0)

    run_visualization(generate_maze_prisms,algo_a_star, canvas ,height, walls,root)

    root.mainloop()