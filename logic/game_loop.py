import pygame
from models.character import Character
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class GameLoop:
    def __init__(self):
        # * Inicializar pygame
        pygame.init()
        # * Inicializar el reloj
        self.clock = pygame.time.Clock()
        # * Inicializar la pantalla
        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # * Establecer el título de la ventana
        pygame.display.set_caption("Mi Primer Juego")

        # * Instancia del personaje
        self.character = Character()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()

            # Limpiar la pantalla
            self.SCREEN.fill((0, 0, 0))

            # Dibujar el personaje
            self.character.handle_input(keys)
            self.character.draw(self.SCREEN)

            # Actualizar la pantalla
            pygame.display.flip()

            # Limitar la cantidad de fotogramas por segundo
            self.clock.tick(30)
