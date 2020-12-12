def main_menu(Dificultad):
    from Instructions_Function import instructions
    from Select_Char_Function import select_ship
    import pygame

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    pygame.init()


    size = (448, 576)
    screen = pygame.display.set_mode(size)
    blink = 0
    flash = False


    #Importing images, sounds, backgrounds
    pygame.display.set_caption("2020")
    pygame.mixer.music.load('Menu.mp3')
    pygame.mixer.music.play(-1)
    background_image = pygame.image.load("blank.png").convert()
    click = pygame.mixer.Sound("click.wav")

    play = pygame.image.load('play.png')
    play1 = pygame.image.load('play1.png')
    instructionsbutton = pygame.image.load('instructions.png')
    instructionsbutton1 = pygame.image.load('instructions1.png')
    quitbutton = pygame.image.load('quit.png')
    quitbutton1 = pygame.image.load('quit1.png')

    mouse_click = [0,0]

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click = pygame.mouse.get_pos()

        if done == False:
            # --- Game logic should go here
            time = (pygame.time.get_ticks()/1000)
            #Returns mouse position
            mouse = pygame.mouse.get_pos()


            screen.fill(BLACK)

            #Start up animation.
            if time >=2 and time <=2.5:
                background_image = pygame.image.load("0p.png").convert()
            if time >2.5 and time <=3:
                background_image = pygame.image.load("1p.png").convert()
            if time >3 and time <=3.5:
                background_image = pygame.image.load("2p.png").convert()
            if time >3.5 and time <=4:
                background_image = pygame.image.load("3p.png").convert()
            if time >4 and time <=4.5:
                background_image = pygame.image.load("4p.png").convert()
            if time >4.5 and time <=5:
                background_image = pygame.image.load("5p.png").convert()
            if time >5 and time <=5.5:
                background_image = pygame.image.load("6p.png").convert()
            if time >5.5:
                background_image = pygame.image.load("6p.png").convert()
                flash = True
            screen.blit(background_image, [0, 0])
            #Keeps the text blinking after animation is over
            if flash == True:
                if blink <=30:
                    blink +=1
                    background_image = pygame.image.load("6p.png").convert()
                    screen.blit(background_image, [0, 0])
                if blink >30:
                    blink +=1
                    background_image = pygame.image.load("blank.png").convert()
                    screen.blit(background_image, [0, 0])
                if blink ==40:
                    blink =0
                #Draws play, instructions, and quit button
                #Buttons are sensitive when use puts mouse over top of button, colours will change
                #Will call other functions to navigate
                screen.blit(play,[174,290])
                if 174<mouse[0]<274 and 290<mouse[1]<340:
                    screen.blit(play1,[174,290])
                screen.blit(instructionsbutton,[174,360])
                if 174<mouse[0]<274 and 360<mouse[1]<410:
                    screen.blit(instructionsbutton1,[174,360])
                if 174<mouse_click[0]<274 and 360<mouse_click[1]<410:
                    click.play()
                    instructions(Dificultad)
                    break
                if 174<mouse_click[0]<274 and 290<mouse_click[1]<340:
                    click.play()
                    select_ship(Dificultad)
                    break
                screen.blit(quitbutton,[174,430])
                if 174<mouse[0]<274 and 430<mouse[1]<480:
                    screen.blit(quitbutton1,[174,430])
                if 174<mouse_click[0]<274 and 430<mouse_click[1]<480:
                    pygame.quit()
                    break


            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

    # Close the window and quit.
    pygame.quit()
