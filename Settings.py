import os
import pygame
import tkinter as tk
from csv import reader

root = tk.Tk()


##Escalabilidad para que los archivos de una carpeta se vayan a mi programa
def import_folder(path):
    surface_list = []
    for _, _, img_files in os.walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


def import_map_csv(path):
    terrain_map=[]
    with open(path) as level_map:
        layout = reader(level_map, delimiter= ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
            

##Creacion de la monda esta pa saber la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("Altura de la pantalla:", screen_height)
print("Anchura de la pantalla:", screen_width)

root.destroy()