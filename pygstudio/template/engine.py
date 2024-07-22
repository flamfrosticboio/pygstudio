# // Pygstudio template file created by pygstudio script (Version 1.0) 

# Note: You are free to edit this script

def start(scrs, scrc, wndf, wndn, wndi, fps, vsync):
    import pygame
    import globals
    import script_manager
    
    globals.on_init()
    
    globals.screen = pygame.display.set_mode(scrs, wndf, 0, 0, vsync)
    pygame.display.set_caption(wndn)
    if wndi: pygame.display.set_icon(wndi)
    
    globals.on_init_window()
    script_manager.run()    # you may move this anywhere in the code (prefered NOT in the loop)
    
    globals.running = True
    while globals.running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.running = False
            globals.on_event(event)
        
        globals.screen.fill(scrc)
        globals.on_render(globals.screen)
        globals.clock.tick(fps)
        
    globals.on_exit()