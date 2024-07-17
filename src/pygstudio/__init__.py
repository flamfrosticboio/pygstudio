import pygame as pg
from .globals import GameGlobals
from .binds import BindFunctions

def run(window_size, window_flags = 0, fps = 60, default_screen_color = (255, 255, 255),
        window_name = None, window_icon = None):
    BindFunctions.preinit()
    
    screen = pg.display.set_mode(window_size, window_flags)
    clock = pg.time.Clock()
    
    if window_name: pg.display.set_caption(window_name)
    else: pg.display.set_caption(f"<PYGSTUDIO WINDOW INSTANCE {hex(id(screen))}>")  # seems useless but why not
    if window_icon: pg.display.set_icon(window_icon)
    
    BindFunctions.preload()
    
    GameGlobals._running = True
    while GameGlobals._running:
        for event in pg.event.get():
            if event.type == pg.QUIT: GameGlobals._running = False
        screen.fill(default_screen_color)
        pg.display.flip()
        clock.tick(fps)
        
    BindFunctions.exit()