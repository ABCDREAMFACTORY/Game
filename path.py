from map_generator import load_map,convert_map,get_entrance_position_grid,get_exit_position_grid,create_map
from settings import WIDTH,HEIGHT,WIDTH_SIZE,HEIGHT_SIZE,DIV,WALL

def find_path():
    map = load_map()
    entrance_x,entrance_y = get_entrance_position_grid()
    exit_x,exit_y = get_exit_position_grid()
    print(entrance_x,entrance_y,exit_x,exit_y)

    def gen_positions(x:int,y:int,path:list)-> list:
        positions = []
        for dx,dy in ((-1,0),(1,0),(0,1),(0,-1)):
            if not 0 <= x+dx < DIV or not 0 <= y+dy < DIV or (x+dx,y+dy) in path or map[y+dy][x+dx] == WALL:
                continue
            positions.append((x+dx,y+dy))
        return positions
    
    def explore(x=entrance_x,y=entrance_y,last_position=(entrance_x,entrance_y),path=[(entrance_x,entrance_y)])->tuple[bool,list]:
        print(f"iteration:{x},{y},{last_position},exit:{exit_x},{exit_y}")
        if (x,y) == (exit_x,exit_y):
            return True, path
        
        positions = gen_positions(x,y,path)
        
        if not positions:
            return False, path
        
        length_path = float("inf")
        max_path = path
        found = False
        for pos in positions:
            has_found,new_path = explore(pos[0],pos[1],last_position=(x,y),path=path+[pos])
            if has_found:
                found = True
            if has_found and len(new_path) < length_path:
                length_path = len(new_path)
                max_path = new_path

        return found,max_path
    
    has_found,path = explore()
    if has_found:
        print("Chemin trouvé !")
        print(path)
    else:
        print("no possible path")

create_map()
find_path()

        