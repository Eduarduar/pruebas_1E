import pygame
from utils.asset_loader import load_character_images

class Character:
    def __init__(self):
        self.x = 640
        self.y = 360
        self.image_index = 0
        self.long = 15 # distancia que avanzara 
        self.direction = 1  # 1: right, 0: left
        self.images = load_character_images()
        self.is_moving = False  # Para saber si el personaje se está moviendo

    def move_right(self):
        self.x += self.long
        # Alterna entre las imágenes 1 y 2 cuando el personaje camina a la derecha
        if self.image_index < 1 or self.image_index > 2: # si la imagen actual no es 1 o 2
            self.image_index = 1
        else:
            self.image_index = 2 if self.image_index == 1 else 1 # el index va ser igual a 2 si el index es igual a 1, de lo contrario va ser igual a 1
        self.direction = 1
        self.is_moving = True

    def move_left(self):
        self.x -= self.long
        # Alterna entre las imágenes 4 y 5 cuando el personaje camina a la izquierda
        if self.image_index < 4 or self.image_index > 5:
            self.image_index = 4
        else:
            self.image_index = 5 if self.image_index == 4 else 4
        self.direction = 0
        self.is_moving = True

    def handle_input(self, keys):
        self.is_moving = False  # Reiniciar el estado de movimiento
        if keys[pygame.K_RIGHT]:
            self.move_right()
        elif keys[pygame.K_LEFT]:
            self.move_left()

    def draw(self, screen):
        # Si el personaje no se mueve, se asegura de mostrar la imagen estática según la dirección
        if not self.is_moving:
            if self.direction == 1:
                self.image_index = 0  # Imagen 0 es la estática mirando a la derecha
            else:
                self.image_index = 3  # Imagen 3 es la estática mirando a la izquierda
        screen.blit(self.images[self.image_index], (self.x, self.y))
