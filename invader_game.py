import sys
import pygame

from game.settings import Settings
from game.ship import Ship
from game.bullet import Bullet

# Clase general para el manejo del juego
class InvaderGame:

    #Inicializa el juego
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        #Se crea la resolución del juego para ejecutar en ventana
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        
        #Se crea la resolución del juego para jugar en modo pantalla completa
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        #Titulo del juego
        pygame.display.set_caption("Invader Game")
        self.ship = Ship(self)
        #Grupo para todas las balas activas
        self.bullets = pygame.sprite.Group()
        


    def run_game(self):
        
        #Ciclo general del juego / Actualizaciones a la pantalla
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)


    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        #Cambia el fondo de pantalla por el color que haya en la clase Settings
        self.screen.fill(self.settings.bg_color)

        #Dibuja en cada ciclo las balas
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #Dibuja la nave espacial
        self.ship.blitme()
        #Actualiza la pantalla con las modificaciones más recientes
        pygame.display.flip()

    def _fire_bullet(self):
        #Crea una nueva bala en la posición de la nave
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    #Crea una instancia y ejecuta el juego
    ig = InvaderGame()
    ig.run_game()
