#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Grant
#
# Created:     03/06/2017
# Copyright:   (c) Grant 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def lose(score, highscore,ship_type):
    from Menu_Function import main_menu
    import pygame

    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    if score > highscore:
        highscore = score

    pygame.init()

    size = (448, 576)
    screen = pygame.display.set_mode(size)

    #Returns the mouse position when user clicks
    mouse_click = [0,0]

    #Importing music, images, background
    pygame.display.set_caption("20XX")
    pygame.mixer.music.load('Instructions.mp3')
    pygame.mixer.music.play(-1)
    background_image = pygame.image.load("lose.png").convert()


    play_again = pygame.image.load('play_again.png')
    play_again1 = pygame.image.load('play_again1.png')
    quitbutton = pygame.image.load('quit.png')
    quitbutton1 = pygame.image.load('quit1.png')


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
                gameover = True
                break
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_click = pygame.mouse.get_pos()
        # --- Game logic should go here
        time = (pygame.time.get_ticks()/1000)

        #Returns mouse position
        mouse = pygame.mouse.get_pos()


        screen.fill(BLACK)


        #Draw background image
        screen.blit(background_image,[0,0])
        #Draw play again button
        screen.blit(play_again,[174,380])
        #Change to lighter colour when user hovers over button
        if 174<mouse[0]<274 and 380<mouse[1]<430:
            screen.blit(play_again1,[174,380])
        #appends score and shipt type to a txt file (Highscores.txt)
        if 174<mouse_click[0]<274 and 380<mouse_click[1]<430:
            f=open("Highscores.txt","a")
            f.write(ship_type.upper())
            f.write(" - ")
            f.write(str(score))
            f.write("\n")
            f.close()
            main_menu(highscore)
            break
        #Quit button
        screen.blit(quitbutton,[174,450])
        if 174<mouse[0]<274 and 450<mouse[1]<500:
            screen.blit(quitbutton1,[174,450])
        #appends score and shipt type to a txt file (Highscores.txt)
        if 174<mouse_click[0]<274 and 450<mouse_click[1]<500:
            f=open("Highscores.txt","a")
            f.write(ship_type.upper())
            f.write(" - ")
            f.write(str(score))
            f.write("\n")
            f.close()
            pygame.quit()
            break

        font = pygame.font.SysFont('Calibri', 33, True, False)
        your_score = font.render("Score:",True,WHITE)
        score_text = font.render(str(score),True,WHITE)
        screen.blit(your_score, [130, 260])
        screen.blit(score_text, [290, 260])
        your_highscore = font.render("Highscore:",True,WHITE)
        highscore_text = font.render(str(highscore),True,WHITE)
        screen.blit(your_highscore, (130, 310))
        screen.blit(highscore_text, [290, 310])
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)
    # Close the window and quit.
    pygame.quit()