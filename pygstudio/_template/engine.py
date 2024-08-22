# // Pygstudio template file created by pygstudio script (Version 2.0)
# ? You are free to edit this script


def start():
    import pygame, globals, script_manager

    pygame.display.set_caption(globals.WINDOW_TITLE)
    if globals.WINDOW_ICON:
        pygame.display.set_icon(globals.WINDOW_ICON)

    script_manager.run()

    globals.running = True
    while globals.running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.running = False
            globals.on_event(event)

        globals.screen.fill(globals.SCREEN_BACKGROUND)
        globals.on_render(globals.screen)

        pygame.display.flip()
        globals.clock.tick(globals.FPS)

    globals.on_exit()
