from utils import get_direction_and_didnt_has_wall,reconstruct_path

def h(i,j,final_x,final_y):
    return abs(final_x-i)+abs(final_y-j)

def get_cost(i,j,final_x,final_y,g):
    return g[(i,j)]+h(i,j,final_x,final_y)

def algo_a_star(walls,final_x,final_y,ROWS):
    nodes=[(0,0)]
    visited=set()
    visited.add((0,0))

    g={(0,0):0}
    search_order=[]
    came_from={}

    def find_best_node(final_x,final_y):
        best=float("inf")
        best_cost=float("inf")

        for x,y in nodes:
            cost=get_cost(x,y,final_x,final_y,g)
            if cost<best_cost:
                best_cost=cost
                best=(x,y)
        
        return best
    
    
    def do_recursive_search(final_x,final_y,visited,ROWS):
        x,y=find_best_node(final_x,final_y)
        nodes.remove((x,y))
        search_order.append((x,y))

        if (x,y)==(final_x,final_y):
            return (x,y)

        for dx,dy in get_direction_and_didnt_has_wall(x,y,walls,visited,ROWS):
            nx,ny=x+dx,y+dy

            if (nx,ny) not in visited:

                g[(nx,ny)]=g[(x,y)]+1
                nodes.append((nx,ny))
                visited.add((nx,ny))

                came_from[(nx,ny)]=(x,y)
        
        return do_recursive_search(final_x,final_y,visited,ROWS)
    
    
    
    current=do_recursive_search(final_x,final_y,visited,ROWS)
    #print(search_order,reconstruct_path(current))
    
    return search_order,reconstruct_path(current , came_from)



