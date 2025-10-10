import pygame
from settings import *
from entities import Wall, Player
from map_generator import create_map, load_map, convert_map

class Game:
    def __init__(self):
        print("\n" * 10)
        # Pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.clock = pygame.time.Clock()
        self.running = True

        # Initialization
        self.entrance, self.exit = create_map()
        self.objects = convert_map(load_map())
        self.player = Player(self.entrance.rect.x, self.entrance.rect.y, WIDTH_SIZE, HEIGHT_SIZE)
    
    #Main game methods
    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self):
        """Handles all game events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.entrance,self.exit = create_map()
                    self.objects = convert_map(load_map())
                    self.player.rect.x = self.entrance.rect.x
                    self.player.rect.y = self.entrance.rect.y

    def update(self):
        """Updates the game state."""
        dx,dy = self.keys()
        self.try_move_player(dx, dy)
    
    def draw(self):
        """Draws all game elements on the screen."""
        self.screen.fill((255, 255, 255))
        self.show_map(self.objects)
        self.player.show(self.screen)
        pygame.display.flip()

    # Helper methods
    def keys(self):
        """Returns the direction of movement based on key presses."""
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1
        elif keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1
        return dx, dy
    
    def try_move_player(self, dx: int, dy: int) -> None:
        """Attempts to move the player in the specified direction if no wall is present."""
        if dx == 0 and dy == 0:
            return

        new_x = self.player.rect.x + dx * WIDTH_SIZE
        new_y = self.player.rect.y + dy * HEIGHT_SIZE

        if new_x < 0 or new_x >= WIDTH or new_y < 0 or new_y >= HEIGHT:
            return

        grid_x = new_x // WIDTH_SIZE
        grid_y = new_y // HEIGHT_SIZE

        cell = self.objects[grid_y][grid_x]
        if isinstance(cell, Wall):
            return

        self.player.move(dx, dy, WIDTH_SIZE, HEIGHT_SIZE)

    def show_map(self, objects: list) -> None:
        """Renders the map objects on the screen."""
        for row in objects:
            for obj in row:
                if obj and hasattr(obj, 'show'):
                    obj.show(self.screen)
