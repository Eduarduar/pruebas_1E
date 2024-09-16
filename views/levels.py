import pygame
from models.character import Character
from utils.asset_loader import load_backgroud_levels
from logic.move_backbround import move_background

class Levels: 
    def __init__(self, screan):
        self.screen = screan
        self.clock = pygame.time.Clock()
        self.statusLevels = {
            "level1": True,
            "level2": False,
            "level3": False
        }

        self.background = load_backgroud_levels()
        self.backgroundPos = {
            "x": 0,
            "y": 0
        }

        # * Creamos el personaje
        self.character = Character(onlyScreen=True ,x=240, y=565)

    def run(self):

        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            move_character = self.character.handle_input(keys)
            if move_character != False:
                move_background(self.screen, self.background, self.backgroundPos, move_character)
            else:
                move_background(self.screen, self.background, self.backgroundPos, 0)

            # * Dibujamos el personaje
            self.character.draw(self.screen)

            self.clock.tick(60)
            pygame.display.flip()