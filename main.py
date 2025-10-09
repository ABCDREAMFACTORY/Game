
import pygame
from settings import *
from entities import Wall,Player
from map_generator import create_map,load_map,convert_map

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
print("\n"*10)


def show_map(objects:list) -> None:
    for line in objects:
        for object in line:
            if object is None or not hasattr(object, 'show'):
                continue

            object.show(screen)

def keys():
    keys = pygame.key.get_pressed()
    dx,dy = 0,0
    if keys[pygame.K_UP]:
        dy = -1
    elif keys[pygame.K_DOWN]:
        dy = 1
    elif keys[pygame.K_LEFT]:
        dx = -1
    elif keys[pygame.K_RIGHT]:
        dx = 1
    return dx,dy

def try_move_player(dx: int, dy: int, objects: list, player: Player) -> None:
    if dx == 0 and dy == 0:
        return

    new_x = player.rect.x + dx * WIDTH_SIZE
    new_y = player.rect.y + dy * HEIGHT_SIZE

    if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:
        return

    grid_x = new_x // WIDTH_SIZE
    grid_y = new_y // HEIGHT_SIZE

    cell = objects[grid_y][grid_x]
    if isinstance(cell, Wall):
        return

    player.move(dx, dy,WIDTH_SIZE,HEIGHT_SIZE)



#initialization
entrance , exit = create_map()
objects = convert_map(load_map())
player = Player(entrance.rect.x,entrance.rect.y,WIDTH_SIZE,HEIGHT_SIZE)



#Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                entrance,exit = create_map()
                objects = convert_map(load_map())
                player.rect.x = entrance.rect.x
                player.rect.y = entrance.rect.y

    screen.fill((200,200,200))



    dx,dy = keys()
    try_move_player(dx,dy,objects,player)

    show_map(objects)
    player.show(screen)



    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60