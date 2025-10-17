import math

WIDTH = 1280
HEIGHT = 720
BLACK = (0,0,0)
DIV = 10
WIDTH_SIZE = math.ceil(WIDTH / DIV)
HEIGHT_SIZE = math.ceil(HEIGHT / DIV)
WALL = "w"
ENTRANCE = "e"
EXIT = "x"
EMPTY = "."
FPS = 15