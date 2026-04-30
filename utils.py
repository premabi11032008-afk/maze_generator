DIRECTIONS=[(1,0),(-1,0),(0,1),(0,-1)]

get_direction_dictionary = {
    (1,0): "bottom",
    (-1,0): "top",
    (0,1): "right",
    (0,-1): "left"
}

def get_available_direction(i,j,visited,ROWS):
    available=[]
    for dx,dy in DIRECTIONS:
        nx,ny=i+dx,j+dy

        if nx<0 or ny<0 or nx>=ROWS or ny>=ROWS:
            continue
            
        if (nx,ny) in visited:
            continue
        
        available.append((dx,dy))
    
    return available