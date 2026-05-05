from utils import get_available_direction,get_direction_dictionary
import random as rd

def generate_maze_dfs(walls, ROWS):
    visited = set()
    path = [(0, 0)]
    visited.add((0, 0))

    while path:
        i, j = path[-1]
        directions = get_available_direction(i, j, visited, ROWS)

        if not directions:
            path.pop()
            continue

        dx, dy = rd.choice(directions)
        ni, nj = i + dx, j + dy

        walls[i][j][get_direction_dictionary[(dx,dy)]] = False
        walls[ni][nj][get_direction_dictionary[(-dx,-dy)]] = False

        visited.add((ni, nj))
        path.append((ni, nj))

        yield (visited,walls)