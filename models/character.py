import pygame
from utils.asset_loader import load_character_images

class Character:
    def __init__(self, onlyScreen=False, x=640, y=360):
        self.x = x
        self.y = y
        self.start_y = y  # Posición original en Y para controlar el aterrizaje
        self.onlyScreen = onlyScreen  # Para saber si el personaje solo se puede mover dentro de la pantalla
        self.image_index = 0
        self.long = 0  # distancia que avanzará 
        self.direction = 1  # 1: derecha, 0: izquierda
        self.images = load_character_images()
        self.is_moving = False  # Para saber si el personaje se está moviendo

        # Variables para el salto
        self.is_jumping = False  # Controla si el personaje está saltando
        self.is_falling = False  # Controla si el personaje está cayendo
        self.jump_speed = 15  # Velocidad de salto
        self.fall_speed = 7  # Velocidad de caída
        self.jump_height = 150  # Altura máxima del salto
        self.jump_offset = 0  # Para controlar cuánto ha saltado

    def move_right(self):
        if self.onlyScreen and self.x > 1280 - 60:
            return
        self.x += self.long
        if self.image_index < 1 or self.image_index > 2:  # si la imagen actual no es 1 o 2
            self.image_index = 1
        else:
            self.image_index = 2 if self.image_index == 1 else 1  # Alterna entre las imágenes 1 y 2
        self.direction = 1
        self.is_moving = True

    def move_left(self):
        if self.onlyScreen and self.x < 10:
            return
        self.x -= self.long
        if self.image_index < 4 or self.image_index > 5:
            self.image_index = 4
        else:
            self.image_index = 5 if self.image_index == 4 else 4  # Alterna entre las imágenes 4 y 5
        self.direction = 0
        self.is_moving = True

    def jump(self):
        # Solo permite saltar si el personaje no está saltando ni cayendo
        if not self.is_jumping and not self.is_falling:
            self.is_jumping = True
            self.jump_offset = 0  # Reinicia el progreso del salto

    def apply_gravity(self):
        if self.is_jumping:
            if self.jump_offset < self.jump_height:  # Mientras no alcance la altura máxima
                self.y -= self.jump_speed
                self.jump_offset += self.jump_speed
            else:
                self.is_jumping = False  # Comienza a caer cuando alcanza la altura máxima
                self.is_falling = True  # Activa el estado de caída
        elif self.is_falling:
            self.y += self.fall_speed  # Aplica gravedad para bajar
            if self.y >= self.start_y:  # Si llega al suelo
                self.y = self.start_y  # Corrige para que no sobrepase el suelo
                self.is_falling = False  # Deja de caer, el personaje está en el suelo

    def handle_input(self, keys):
        # los returns son para que el fondo de pantalla sepas si se mueve a la derecha o izquierda
        self.is_moving = False  # Reiniciar el estado de movimiento
        
        # Permitir múltiples teclas presionadas
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]: # Si se presionan las dos teclas horizontales, no se mueve
            return False

        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_UP]:
            self.jump()

        # Determina el valor de retorno basado en el movimiento
        if keys[pygame.K_RIGHT]:
            return 10
        elif keys[pygame.K_LEFT]:
            return -10
        return False

    def draw(self, screen):
        if not self.is_moving:
            if self.direction == 1:
                self.image_index = 0  # Imagen estática mirando a la derecha
            else:
                self.image_index = 3  # Imagen estática mirando a la izquierda
        screen.blit(self.images[self.image_index], (self.x, self.y))

    def update(self):
        self.apply_gravity()  # Aplica la gravedad en cada frame para controlar el salto
