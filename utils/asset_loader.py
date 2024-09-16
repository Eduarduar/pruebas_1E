import pygame
import os

def load_character_images():
    # Carpeta donde se encuentran las imágenes del personaje
    image_folder = os.path.join("assets", "images", "sprites", "personaje")
    
    # Cargar las imágenes del personaje en una lista
    images = [
        pygame.image.load(os.path.join(image_folder, f"personaje{i}.png"))
        for i in range(1, 7)
    ]
    
    # Devolver la lista de imágenes del personaje
    return images

def load_buttons_menu_primary():
    # Carpeta donde se encuentran las imágenes de los botones
    folder_button_config = os.path.join("assets", "images", "buttons", "configuración")
    folder_butotn_play = os.path.join("assets", "images", "buttons", "jugar")
    folder_button_exit = os.path.join("assets", "images", "buttons", "salir")
    
    # Cargar las imágenes de los botones en una lista
    button_config = [
        pygame.image.load(os.path.join(folder_button_config, f"button{i}.png"))
        for i in range(1, 3)
    ]

    button_play = [
        pygame.image.load(os.path.join(folder_butotn_play, f"button{i}.png"))
        for i in range(1, 3)
    ]

    button_exit = [
        pygame.image.load(os.path.join(folder_button_exit, f"button{i}.png"))
        for i in range(1, 3)
    ]
    
    # Devolver la lista de imágenes de los botones
    return button_config, button_play, button_exit

def load_backgroud_levels():
    # Carpeta donde se encuentran las imágenes de los fondos
    folder_backgrounds = os.path.join("assets", "images", "backgrounds")
    
    background = pygame.image.load(os.path.join(folder_backgrounds, f"levels.png"))
    
    # Devolver la lista de imágenes de los fondos
    return background