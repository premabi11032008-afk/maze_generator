from utils import get_available_direction,get_direction_dictionary
import random as rd

def get_neighbours(cell_x,cell_y,visited , ROWS):
    neighbours=[]

    for dx,dy in get_available_direction(cell_x,cell_y,visited,ROWS):
        nx,ny=cell_x+dx,cell_y+dy
        neighbours.append((nx,ny))

    return neighbours

def generate_maze_prisms(walls, ROWS):
    visited = set()
    front=[]

    start=(0,0)
    visited.add(start)

    for nx,ny in get_neighbours(*start,visited,ROWS):
        front.append((start,(nx,ny)))

    while front:
        start,end=rd.choice(front)
        front.remove((start,end))

        if end in visited:
            continue

        for nx,ny in get_neighbours(*end,visited,ROWS):
            front.append((end,(nx,ny)))
        
        dx = end[0] - start[0]
        dy = end[1] - start[1]

        walls[start[0]][start[1]][get_direction_dictionary[(dx, dy)]] = False
        walls[end[0]][end[1]][get_direction_dictionary[(-dx, -dy)]] = False

        visited.add(end)

        yield (visited,walls)        






    