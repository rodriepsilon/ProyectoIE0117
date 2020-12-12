def instructions(Dificultad):
    from Menu_Function import main_menu
    import pygame

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    pygame.init()


    size = (448, 576)
    screen = pygame.display.set_mode(size)

    #Detect where the mouse position is when user clicks
    mouse_click = [0,0]
    #Importing background, music, pictures etc
    pygame.display.set_caption("Instructions")
    pygame.mixer.music.load('Instructions.mp3')
    pygame.mixer.music.play(-1)
    background_image = pygame.image.load("lorep.png").convert()


    back = pygame.image.load('back.png')
    back1 = pygame.image.load('back1.png')
    instructions = pygame.image.load('instructions.png')
    instructions1 = pygame.image.load('instructions1.png')



    done = False


    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click = pygame.mouse.get_pos()
        # --- Game logic should go here
        time = (pygame.time.get_ticks()/1000)
        #Collect mouse position so buttons can work
        mouse = pygame.mouse.get_pos()


        screen.fill(BLACK)


        #Drawing background image
        screen.blit(background_image,[0,0])
        #Drawing back button
        screen.blit(back,[330,505])
        if 330<mouse[0]<430 and 505<mouse[1]<555:
            #If mouse hovers over button, change colour to recognize the user is over the button
            screen.blit(back1,[330,505])
        if 330<mouse_click[0]<430 and 505<mouse_click[1]<555:
            #If clicked, run menu function
            main_menu(Dificultad)
            break

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()
