import sys
import pygame

from settings import Settings
from ship import Ship

# Clase general para el manejo del juego
class InvaderGame:

    #Inicializa el juego
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #Se crea la resolución del juego
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        #Titulo del juego
        pygame.display.set_caption("Invader Game")
        self.ship = Ship(self)
        


    def run_game(self):
        
        #Ciclo general del juego / Actualizaciones a la pantalla
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False




    def _update_screen(self):
        #Cambia el fondo de pantalla por el color que haya en la clase Settings
        self.screen.fill(self.settings.bg_color)
        #Dibuja la nave espacial
        self.ship.blitme()
        #Actualiza la pantalla con las modificaciones más recientes
        pygame.display.flip()


if __name__ == '__main__':
    #Crea una instancia y ejecuta el juego
    ig = InvaderGame()
    ig.run_game()
