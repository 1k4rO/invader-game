import sys
import pygame

# Clase general para el manejo del juego
class InvaderGame:

    #Inicializa el juego
    def __init__(self):
        pygame.init()

        #Se crea la resolución del juego
        self.screen = pygame.display.set_mode((1200,800))
        #Titulo del juego
        pygame.display.set_caption("Invader Game")



    def run_game(self):
        
        #Ciclo general del juego / Actualizaciones a la pantalla
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Actualiza la pantalla con las modificaciones más recientes
            pygame.display.flip()


if __name__ == '__main__':
    #Crea una instancia y ejecuta el juego
    ig = InvaderGame()
    ig.run_game()
