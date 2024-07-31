# // Pygstudio template file created by pygstudio script (Version 1.2) 
# ? You are free to edit this script

def start(screen_size, screen_fill_color, window_flags, window_title, window_icon, fps, vsync):
    import pygame
    import globals
    import script_manager
    
    globals.screen = pygame.display.set_mode(screen_size, window_flags, 0, 0, vsync)
    pygame.display.set_caption(window_title)
    if window_icon: pygame.display.set_icon(window_icon)
    
    globals.on_init()
    script_manager.run()
    
    globals.running = True
    while globals.running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.running = False
            globals.on_event(event)
        
        globals.screen.fill(screen_fill_color)
        globals.on_render(globals.screen)
        
        pygame.display.flip()
        globals.clock.tick(fps)
        
    globals.on_exit()