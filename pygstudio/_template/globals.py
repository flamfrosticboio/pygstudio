# // Pygstudio template file created by pygstudio script (Version 2.1)
# ? You are free to edit this script

import pygame

########### For 'engine.py' ################
WINDOW_ICON = None      # ? if specified, it must be 'pygame.Surface'
WINDOW_TITLE = "$MYPYGSTUDIOGAME"
SCREEN_BACKGROUND = (255, 255, 255)
FPS = 60

running: bool = False
clock = pygame.time.Clock()
screen_size = pygame.Rect(0, 0, 720, 480)
screen = pygame.display.set_mode(screen_size.size)
#############################################
def on_event(event: pygame.event.Event) -> None:
    # * Bindable function for handling every event (in a for loop).
    pass


def on_render(screen: pygame.Surface) -> None:
    # * Bindable function for rendering objects to screen.
    pass


def on_exit():
    # * Bindable function for closing the program.
    pass
#############################################

# * Others (put other variables here)
