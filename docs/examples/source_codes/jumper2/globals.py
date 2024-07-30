# // Pygstudio template file created by pygstudio script (Version 1.0)

# Note: You are free to edit this script as it is intended to be edited
#       You may also delete other comments in this script
#       Add other variables here as globals

from typing import Optional
import pygame

running: bool = False

clock: pygame.time.Clock = pygame.time.Clock()
screen: Optional[pygame.Surface] = None


# === Optional functions ===

# def get_screen() -> Optional[pygame.Surface]:
#     if screen is None and debug_mode == True:
#         print("PYGSTUDIO WARNING: Game is not yet initialized!")
#     return screen

# === Bindable functions (Required most of the time) ===
# These bindable functions can be setted outside this script
# and add initialization code at 'on_init()' function that will
# set these functions outside the script

def on_event(event: pygame.event.Event) -> None:
    # This bindable function is called in every event.
    pass

def on_render(screen: pygame.Surface) -> None:
    # This bindable function is executed in every rendered step.
    pass

def on_init() -> None:
    # This bindable function is executed before the window initialization
    
    # === Outside setter code template (to make your day easier) === # 
    # from scripts import SCRIPTNAME
    pass

def on_init_window():
    # This bindable function is executed after the window initialization
    pass

def on_exit():
    # This bindable function is executed when the game exits
    pass