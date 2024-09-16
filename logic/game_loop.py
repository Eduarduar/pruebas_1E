import pygame
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from views.menuPrimary import MenuPrimary

class GameLoop:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mi Primer Juego")

        # Crear instancia del menú
        self.menu = MenuPrimary(self.SCREEN)
    
    def run(self):
        # Ejecutar el menú primero
        self.menu.run()
