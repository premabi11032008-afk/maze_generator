from utils import get_direction_and_didnt_has_wall,reconstruct_path

def queue_algorithm(walls,final_x,final_y,ROWS):
    queue=[(0,0)]
    came_from={}

    visited=set()
    visited.add((0,0))

    search_order=[(0,0)]
    running=True

    while running:
        x,y=queue.pop(0)

        for dx,dy in get_direction_and_didnt_has_wall(x,y,walls,visited,ROWS):
            nx,ny=x+dx,y+dy
            search_order.append((nx,ny))
            visited.add((nx,ny))

            came_from[(nx,ny)]=(x,y)
            if (nx,ny)==(final_x,final_y):
                running=False
                break

            queue.append((nx,ny))
    
    return search_order,reconstruct_path((final_x,final_y),came_from)
