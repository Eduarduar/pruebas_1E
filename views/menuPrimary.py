import pygame
from models.components.button import Button
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT  
from utils.asset_loader import load_buttons_menu_primary
from views.levels import Levels

class MenuPrimary:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Definir el estilo de los botones
        base_color = (255, 255, 255)  # Blanco
        hovering_color = (255, 0, 0)  # Rojo cuando el mouse pasa sobre el botón
        
        button_config, button_play, button_exit = load_buttons_menu_primary()

        # Crear botones
        self.button_play = Button(
            image1          = pygame.transform.scale(button_play[0], (350, 100)),
            pos             = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100),
            text_input      = "",
            font            = 75,
            base_color      = base_color,
            hovering_color  = hovering_color,
            image2          = pygame.transform.scale(button_play[1], (350, 100))
        )

        self.button_config = Button(
            image1          = pygame.transform.scale(button_config[0], (480, 100)),
            pos             = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 25),
            text_input      = "",
            font            = 75,
            base_color      = base_color,
            hovering_color  = hovering_color,
            image2          = pygame.transform.scale(button_config[1], (480, 100))
        )

        self.button_exit = Button(
            image1          = pygame.transform.scale(button_exit[0], (350, 100)),
            pos             = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150),
            text_input      = "",
            font            = 75,
            base_color      = base_color,
            hovering_color  = hovering_color,
            image2          = pygame.transform.scale(button_exit[1], (350, 100))
        )
        
    def run(self):
        while self.running:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    return
                
                # Detectar clic en los botones
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_play.checkForInput(mouse_pos):
                        print("Play clicked")
                        levels = Levels(self.screen)
                        levels.run()
                    elif self.button_exit.checkForInput(mouse_pos):
                        print("Exit clicked")
                        pygame.quit()
                        return
            
            # Limpiar la pantalla
            self.screen.fill((50, 50, 50))  # Color de fondo
            
            # Actualizar y mostrar botones
            self.button_play.changeColor(mouse_pos)
            self.button_config.changeColor(mouse_pos)
            self.button_exit.changeColor(mouse_pos)

            self.button_play.update(self.screen)
            self.button_config.update(self.screen)
            self.button_exit.update(self.screen)

            # Actualizar pantalla
            pygame.display.flip()

            # Limitar fotogramas por segundo
            self.clock.tick(30)
