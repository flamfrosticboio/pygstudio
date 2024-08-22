# // Pygstudio template file created by pygstudio script (Version 1.2.1)
# ? You are free to edit this script

import pygame

# ! Important variables for the engine
running: bool = False
clock = pygame.time.Clock()
# The screen is None if the window is not initialized
screen = None   # type: pygame.Surface | None

def on_event(event: pygame.event.Event) -> None:
    # * This bindable function is called in every event.
    pass

def on_render(screen: pygame.Surface) -> None:
    # * This bindable function is executed in every rendered step.
    pass

def on_init(screen: pygame.Surface):
    # * This bindable function is executed after the window initialization
    pass

def on_exit():
    # * This bindable function is executed when the game exits
    pass