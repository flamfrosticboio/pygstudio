# // Pygstudio template file created by pygstudio script (Version 1.1.1) 
# ? You are free to edit this script, especially comments

SCREEN_SIZE = (680, 420)
SCREEN_BACKGROUND = (255, 255, 255)

WINDOW_TITLE = "$MYPYGSTUDIOGAME"

# Use pygame.load.image() for setting window_icon. 
# Ex: WINDOW_ICON = pygame.image.load("mygame.png")
WINDOW_ICON = None      

# To use this config, you must import pygame and perform or operation on flags
# Example: pygame.RESIZABLE | pygame.OPENGL | ...
# * Tips: pygame.RESIZABLE = 16
WINDOW_FLAGS = 0

# Determines the frames per second. Use 0 for no limit
FPS = 60
VSYNC = True

import engine
engine.start(SCREEN_SIZE, SCREEN_BACKGROUND, WINDOW_FLAGS,
             WINDOW_TITLE, WINDOW_ICON, FPS, VSYNC)