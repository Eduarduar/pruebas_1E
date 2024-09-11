import pygame
import os

def load_character_images():
    # Carpeta donde se encuentran las imágenes del personaje
    image_folder = os.path.join("assets", "sprites", "personaje")
    
    # Cargar las imágenes del personaje en una lista
    images = [
        pygame.image.load(os.path.join(image_folder, f"personaje{i}.png"))
        for i in range(1, 7)
    ]
    
    # Devolver la lista de imágenes del personaje
    return images
