import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Clase para montar un solo alien"""

    def __init__(self, ig_game):
        super().__init__()
        self.screen = ig_game.screen

        self.image = pygame.image.load('images/rect1795.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)