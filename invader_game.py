import sys
import pygame

from game.settings import Settings
from game.ship import Ship
from game.bullet import Bullet
from game.alien import Alien

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
        #Grupo para los aliens que están en pantalla
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        


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
        

        self.aliens.draw(self.screen)
        #Actualiza la pantalla con las modificaciones más recientes
        pygame.display.flip()

    def _fire_bullet(self):
        #Crea una nueva bala en la posición de la nave
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _create_fleet(self):
        """Crea todos los aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        count=0
        while current_y < (self.settings.screen_height/2):
            
            while current_x < (self.settings.screen_width -3 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 3*alien_width
            if(count%2==1):
                current_x = 1.5*alien_width
            else:
                current_x = 0
            count += 1
            current_y += 2*alien_height

    def _create_alien(self, x_position, y_position):
        """Crea un solo alien"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

if __name__ == '__main__':
    #Crea una instancia y ejecuta el juego
    ig = InvaderGame()
    ig.run_game()
