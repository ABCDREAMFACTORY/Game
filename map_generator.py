from settings import *
import random as r
from entities import Wall,Entrance,Exit

def create_map()-> tuple[Entrance,Exit]:
    """Creates a new map and places the entrance and exit."""
    print("Creating map...")
    with open("map.txt","w") as f:
        

        f.write(WALL*DIV + "\n")

        for line in range(DIV-2):
            f.write("w")
            for col in range(DIV-2):
                id = r.randint(0,300)
                if id%3 == 0:
                    f.write(WALL)
                else:
                    f.write(EMPTY)
            f.write(WALL+"\n")

        f.write(WALL*DIV + "\n")

    place_entrance_exit(load_map())

    print("Map created")
    print("-"*20)

    for y,line in enumerate(load_map()):
        for x,obj in enumerate(line):
            if obj == "e":
                entrance = Entrance(x*WIDTH_SIZE,y*HEIGHT_SIZE,WIDTH_SIZE,HEIGHT_SIZE)
            elif obj == "x":
                exit = Exit(x*WIDTH_SIZE ,y*HEIGHT_SIZE,WIDTH_SIZE,HEIGHT_SIZE)
    return entrance, exit

def place_entrance_exit(map:list) -> None:
    """Places the entrance and exit in random free spaces on the map."""
    free = [(x,y) for x in range(DIV) for y in range(DIV) if map[y][x] == "."]
    print("Free spaces:",len(free))
    entrance = r.choice(free)
    map[entrance[1]][entrance[0]] = ENTRANCE
    free.remove(entrance)

    exit = r.choice(free)
    map[exit[1]][exit[0]] = EXIT

    with open("map.txt","w") as f:
        for line in map:
            f.write("".join(line) + "\n")


def load_map()-> list:
    """Loads the map from the map.txt file."""
    with open("map.txt","r") as f:
        walls = [[None for _ in range(DIV)] for _ in range(DIV)]
        for y,line in enumerate(f.readlines()):
            for x,column in enumerate(line.strip()):
                walls[y][x] = column
    return walls

def convert_map(map:list) -> list:
    """Converts the map from characters to objects."""
    for y,line in enumerate(map):
        for x,column in enumerate(line):
            if column == WALL:
                map[y][x]= Wall(x*WIDTH_SIZE,y*HEIGHT_SIZE,WIDTH_SIZE,HEIGHT_SIZE)
            elif column == ENTRANCE:
                map[y][x]= Entrance(x*WIDTH_SIZE,y*HEIGHT_SIZE,WIDTH_SIZE,HEIGHT_SIZE)
            elif column == EXIT:
                map[y][x]= Exit(x*WIDTH_SIZE,y*HEIGHT_SIZE,WIDTH_SIZE,HEIGHT_SIZE)       
    return map
