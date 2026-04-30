import tkinter as tk
import random as rd

ROWS=20
walls=[[{"top":True,"bottom":True,"right":True,"left":True} for _ in range(ROWS)]for _ in range(ROWS)]
visited=[[False for _ in range(ROWS)]for _ in range(ROWS)]
visited[0][0]=True
path=[(0,0)]
height=800//ROWS

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

DIRECTIONS=[(1,0),(-1,0),(0,1),(0,-1)]
get_direction_dictionary = {
    (1,0): "bottom",
    (-1,0): "top",
    (0,1): "right",
    (0,-1): "left"
}

def get_available_direction(i,j):
    available=[]

    for dx,dy in DIRECTIONS:
        nx,ny=i+dx,j+dy

        if nx<0 or ny<0 or nx>=ROWS or ny>=ROWS:
            continue
            
        if visited[nx][ny]==True:
            continue
        
        available.append((dx,dy))
    
    return available


def update_canvas(canvas):
    if path==[]:
        return

    last_i,last_j=path[-1]
    directions=get_available_direction(last_i,last_j)

    #print(last_i,last_j,directions)
    if not directions:
        path.pop()
        root.after(100,lambda:update_canvas(canvas))
        return

    dx,dy=rd.choice(directions)
    nx,ny=last_i+dx,last_j+dy

    visited[nx][ny]=True

    walls[last_i][last_j][get_direction_dictionary[(dx,dy)]]=False
    walls[nx][ny][get_direction_dictionary[(-dx,-dy)]]=False

    path.append((nx,ny))

    canvas.delete("all")

    for i in range(ROWS):
        for j in range(ROWS):
            if visited[i][j]:
                x, y = grid_to_pixel(i, j)
                draw_square(x, y, canvas,"green",walls[i][j])

    root.after(100, lambda: update_canvas(canvas))

root=tk.Tk()
root.geometry("800x800")
root.title("Mace")

canvas=tk.Canvas(root)
canvas.pack(expand=True,fill="both")

update_canvas(canvas)

root.mainloop()