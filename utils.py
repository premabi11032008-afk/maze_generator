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

def grid_to_pixel(i, j , height):
    return (j * height + height / 2, i * height + height / 2)

def draw_square(x,y, canvas , height ,color="green",
                border={"top":False,"bottom":False,"right":False,"left":False}):

    x1, y1 = x - (height / 2), y - (height / 2)
    x2, y2 = x + (height / 2), y + (height /2)

    x1,y1,x2,y2=round(x1),round(y1),round(x2),round(y2)

    canvas.create_rectangle(x1, y1, x2, y2, fill=color,outline="")

    if border["top"]:
        canvas.create_line(x1, y1, x2, y1)

    if border["bottom"]:
        canvas.create_line(x1, y2, x2, y2)

    if border["left"]:
        canvas.create_line(x1, y1, x1, y2)

    if border["right"]:
        canvas.create_line(x2, y1, x2, y2)

def get_direction_and_didnt_has_wall(i,j,walls,visited,ROWS):
    direction=get_available_direction(i,j,visited,ROWS)

    available=[]
    for dx,dy in direction:
        dir=get_direction_dictionary[(dx,dy)]
        if walls[i][j][dir]==False:available.append((dx,dy))
    
    return available

def reconstruct_path(current, came_from):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        path.reverse()
        return path