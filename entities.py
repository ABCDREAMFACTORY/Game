import pygame

class Wall:
    def __init__(self, x, y, width, height,color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def show(self, screen: pygame.Surface) -> None:
        """Draws the wall on the given screen."""
        pygame.draw.rect(screen, self.color, self.rect)


class Entrance:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)
        
    def show(self, screen: pygame.Surface) -> None:
        """Draws the entrance on the given screen."""
        pygame.draw.rect(screen, self.color, self.rect)


class Exit:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)

    def show(self, screen: pygame.Surface) -> None:
        """Draws the exit on the given screen."""
        pygame.draw.rect(screen, self.color, self.rect)

class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def show(self, screen: pygame.Surface) -> None:
        """Draws the player on the given screen."""
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

    def move(self, dx:float, dy:float,width:float,height: float) -> None:
        """Moves the player by the given delta values."""
        self.rect.x += dx * width
        self.rect.y += dy * height