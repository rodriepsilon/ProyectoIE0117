def select_ship(Dificultad):
    from math import sin, cos, pi
    from Menu_Function import main_menu
    import pygame
    import SpaceInvader 
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    displayWidth = 448
    displayHeight = 576
    fpsLimit = 90


    #Just for asthetic purposes
    ring = pygame.image.load("blue_ring.jpg")


    #Import ship images
    ship1 = pygame.image.load("nave.png")
    ship1= pygame.transform.scale(ship1,(174,126))
    ship2 = pygame.image.load("nave3.png")
    ship2= pygame.transform.scale(ship2,(174,126))
    ship3 = pygame.image.load("nave2.png")
    ship3= pygame.transform.scale(ship3,(174,126))
    ship4 = pygame.image.load("nave1.png")
    ship4= pygame.transform.scale(ship4,(174,126))
    ship5 = pygame.image.load("nave4.png")
    ship5= pygame.transform.scale(ship5,(174,126))
    ship6 = pygame.image.load("nave5.png")
    ship6= pygame.transform.scale(ship6,(174,126))
    ship7 = pygame.image.load("nave6.png")
    ship7= pygame.transform.scale(ship7,(174,126))



    #A lot of the coding in this module was from https://www.pygame.org/project-Rotating+Menu-975-.html
    #Thanks to shr4pnell and Francesco Mastellone
    def sinInterpolation(start, end, steps=30):
        values = [start]
        delta = end - start
        for i in range(1, steps):
            n = (pi / 2.0) * (i / float(steps - 1))
            values.append(start + delta * sin(n))
        return values

    class RotatingMenu:
        def __init__(self, x, y, radius, arc=pi*2, defaultAngle=0, wrap=False):
            self.x = x
            self.y = y
            self.radius = radius
            self.arc = arc
            self.defaultAngle = defaultAngle
            self.wrap = wrap

            self.rotation = 0
            self.rotationTarget = 0
            self.rotationSteps = [] #Used for interpolation

            self.items = []
            self.selectedItem = None
            self.selectedItemNumber = 0

        def addItem(self, item):
            self.items.append(item)
            if len(self.items) == 1:
                self.selectedItem = item

        def selectItem(self, itemNumber):
            if self.wrap == True:
                if itemNumber > len(self.items) - 1: itemNumber = 0
                if itemNumber < 0: itemNumber = len(self.items) - 1
            else:
                itemNumber = min(itemNumber, len(self.items) - 1)
                itemNumber = max(itemNumber, 0)

            self.selectedItem.deselect()
            self.selectedItem = self.items[itemNumber]
            self.selectedItem.select()

            self.selectedItemNumber = itemNumber

            self.rotationTarget = - self.arc * (itemNumber / float(len(self.items) - 1))

            self.rotationSteps = sinInterpolation(self.rotation,
                                                  self.rotationTarget, 45)

        def rotate(self, angle):
            """@param angle: The angle in radians by which the menu is rotated.
            """
            for i in range(len(self.items)):
                item = self.items[i]
                n = i / float(len(self.items) - 1)
                rot = self.defaultAngle + angle + self.arc * n

                item.x = self.x + cos(rot) * self.radius
                item.y = self.y + sin(rot) * self.radius

        def update(self):
            if len(self.rotationSteps) > 0:
                self.rotation = self.rotationSteps.pop(0)
                self.rotate(self.rotation)

        def draw(self, display):
            """@param display: A pyGame display object
            """
            for item in self.items:
                item.draw(display)

    class MenuItem:
        def __init__(self, text=""):
            self.text = text

            self.defaultColor = (255,255,255)
            self.selectedColor = (50,50,255)
            self.color = self.defaultColor

            self.x = 0
            self.y = 0 #The menu will edit these

            self.font = pygame.font.Font(None, 17)
            self.image = self.font.render(self.text, True, self.color)
            size = self.font.size(self.text)
            self.xOffset = size[0] / 2
            self.yOffset = size[1] / 2

        def select(self):
            """Just visual stuff"""
            self.color = self.selectedColor
            self.redrawText()

        def deselect(self):
            """Just visual stuff"""
            self.color = self.defaultColor
            self.redrawText()

        def redrawText(self):
            self.font = pygame.font.Font(None, 17)
            self.image = self.font.render(self.text, True, self.color)
            size = self.font.size(self.text)
            self.xOffset = size[0] / 2
            self.yOffset = size[1] / 2

        def draw(self, display):
            display.blit(self.image, (self.x-self.xOffset, self.y-self.yOffset))

    def scrolling_menu():

        #This section was tampered with and customized

        mouse_click = [0,0]
        back = pygame.image.load('back.png')
        back1 = pygame.image.load('back1.png')
        pygame.init()
        pygame.mixer.music.load('select.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        #High tech swiping sound
        swipe_sound = pygame.mixer.Sound("swipe.ogg")
        display = pygame.display.set_mode((displayWidth, displayHeight))
        clock = pygame.time.Clock()

        #Customizes the radius and position of the circular menu
        choice = RotatingMenu(x=225, y=290, radius=180, arc=pi, defaultAngle=pi/2.0)

        #Created a list of all the ships
        names = ["Classic", 'Space','Steel','KappaPride','Ice','Victorious','Cool']
        arwing_number = 0
        for i in range(7):
            #Allows user to scroll through multiple ships
            choice.addItem(MenuItem(names[arwing_number]))
            arwing_number +=1
        choice.selectItem(0)
        #Loop
        done = False
        while not done:
            mouse = pygame.mouse.get_pos()
            #Update stuff

            choice.update()
            background_image = pygame.image.load("char_screen.png").convert()
            display.blit(background_image, [0, 0])
            blue_ring = pygame.transform.scale(ring, (670, 420))
            display.blit(blue_ring,[-97,85])

            #Create a preview blit on screen when user selects ship
            if choice.selectedItemNumber == 0:
                display.blit(ship1,[137,220])
            elif choice.selectedItemNumber == 1:
                display.blit(ship2,[137,220])
            elif choice.selectedItemNumber == 2:
                display.blit(ship3,[137,220])
            elif choice.selectedItemNumber == 3:
                display.blit(ship4,[137,220])
            elif choice.selectedItemNumber == 4:
                display.blit(ship5,[137,220])
            elif choice.selectedItemNumber == 5:
                display.blit(ship6,[137,220])
            elif choice.selectedItemNumber == 6:
                display.blit(ship7,[137,220])
            #Draw stuff

            choice.draw(display)
            display.blit(back,[330,505])
            if 330<mouse[0]<430 and 505<mouse[1]<555:
                display.blit(back1,[330,505])
            if 330<mouse_click[0]<430 and 505<mouse_click[1]<555:
                pygame.mixer.music.set_volume(1)
                main_menu(Dificultad)

            pygame.display.flip() #Show the updated scene
            clock.tick(fpsLimit) #Wait a little

            #Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    done = True
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        choice.selectItem(choice.selectedItemNumber + 1)
                        swipe_sound.play()
                    if event.key == pygame.K_RIGHT:
                        choice.selectItem(choice.selectedItemNumber - 1)
                        swipe_sound.play()
                    if event.key==pygame.K_s:
                        #When user selects a ship, send a variable to the game function and the game starts with users choice of ship
                        print(choice.selectedItemNumber)
                        if choice.selectedItemNumber == 0:
                            #game("classic", Dificultad)
                            SpaceInvader.SpaceInvader(0, "classic")
                        if choice.selectedItemNumber == 1:
                            SpaceInvader.SpaceInvader(0, "space")
                            #Game starts
                            #game("space", Dificultad)
                        if choice.selectedItemNumber == 2:
                            SpaceInvader.SpaceInvader(0, "steel")
                            #Game starts
                            #game("steel", Dificultad)
                        if choice.selectedItemNumber == 3:
                            SpaceInvader.SpaceInvader(1, "kappapride")
                            #Game starts
                            #game("kappapride", Dificultad)
                        if choice.selectedItemNumber == 4:
                            SpaceInvader.SpaceInvader(1, "ice")
                            #Game starts
                            #game("ice", Dificultad)
                        if choice.selectedItemNumber == 5:
                            SpaceInvader.SpaceInvader(2, "victorious")
                            #Game starts
                            #game("victorious", Dificultad)
                        if choice.selectedItemNumber == 6:
                            SpaceInvader.SpaceInvader(2, "cool")
                            #Game starts
                            #game("cool", Dificultad)
                        swipe_sound.play()
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_click = pygame.mouse.get_pos()

    scrolling_menu()
