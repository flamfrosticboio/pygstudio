# // Pygstudio template file created by pygstudio script (Version 2.0)
# ? You are free to edit this script

import pygame

########### For 'engine.py' ################
WINDOW_ICON = None      # ? if specified, it must be 'pygame.Surface'
WINDOW_TITLE = "$MYPYGSTUDIOGAME"
SCREEN_BACKGROUND = (255, 255, 255)
FPS = 60

running: bool = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((720, 480))
#############################################

# * Others (put other variables here)


def on_event(event: pygame.event.Event) -> None:
    # * This bindable function is called in every event.
    pass


def on_render(screen: pygame.Surface) -> None:
    # * This bindable function is executed in every rendered step.
    pass


def on_exit():
    # * This bindable function is executed when the game exits
    pass
