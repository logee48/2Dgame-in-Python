def game():
    # importing libraries
    import pygame
    import math
    import random

    # initializing the constructor
    pygame.init()

    # bg image
    background = pygame.image.load('group 1.png')

    # screen resolution
    res = (1000, 600)

    # opening a window
    screen = pygame.display.set_mode(res)

    # white and black color
    white = (255, 255, 255)
    black = (0, 0, 0)

    # font
    smallfont = pygame.font.SysFont('bold', 40)
    # adding text
    text = smallfont.render('1-player', True, white)
    text1 = smallfont.render('2-players', True, black)
    text2 = smallfont.render('Quit', True, white)

    # one player
    def oneplayer():

        pygame.init()

        # create the screen
        screen = pygame.display.set_mode((1000, 600))

        # white and black color
        white = (255, 255, 255)
        black = (0, 0, 0)

        # font
        smallfont = pygame.font.SysFont('bold', 60)
        # adding text
        text = smallfont.render('Home', True, white)
        text1 = smallfont.render('Restart', True, white)

        # Background
        background = pygame.image.load('applegamebgnew.png')

        # adding title
        pygame.display.set_caption("apple smasher")

        # creating player
        playerImg = pygame.image.load('triangle.png')
        playerX = 470
        playerY = 480
        playerX_change = 0
        playerY_change = 0

        # creating enemy
        enemyImg = []
        enemyX = []
        enemyY = []
        enemyX_change = []
        enemyY_change = []
        num_of_enemies = 10

        for i in range(num_of_enemies):
            enemyImg.append(pygame.image.load('dot.png'))
            enemyX.append(random.randint(40, 40))
            enemyY.append(random.randint(40, 40))
            # enemy x and y axis difference
            enemyX_change.append(1)
            enemyY_change.append(8)

        # Score text
        score_value = 0
        font = pygame.font.Font('freesansbold.ttf', 32)

        # score position
        textX = 10
        testY = 10

        # Game Over text
        over_font = pygame.font.Font('freesansbold.ttf', 64)

        def show_score(x, y):
            score = font.render("Score : " + str(score_value), True, (255, 255, 255))
            screen.blit(score, (x, y))

        def game_over_text():
            over_text = over_font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(over_text, (300, 250))

        def player(x, y):
            screen.blit(playerImg, (x, y))

        def enemy(x, y, i):
            screen.blit(enemyImg[i], (x, y))

        def isCollision(enemyX, enemyY, playerX, playerY):
            distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
            if distance < 27:
                return True
            else:
                return False

        # Game Loop
        while True:

            # RGB = Red, Green, Blue
            screen.fill((0, 0, 0))
            # Background Image
            screen.blit(background, (0, 0))

            # home and restart
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

                # keys for movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        playerY_change = -2
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        playerY_change = 2
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        playerX_change = -2
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        playerX_change = 2

                # checks if a mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 0 <= mouse[0] <= 150 and 550 <= mouse[1] <= 610:
                        game()

                    elif 850 <= mouse[0] <= 1000 and 550 <= mouse[1] <= 610:
                        oneplayer()

            # if mouse is hovered on a button it
            # changes to lighter shade
            # for 1st text
            if 0 <= mouse[0] <= 150 and 550 <= mouse[1] <= 610:
                pygame.draw.rect(screen, black, [0, 550, 150, 50])

            # for 2nd text
            elif 850 <= mouse[0] <= 1000 and 550 <= mouse[1] <= 610:
                pygame.draw.rect(screen, black, [850, 550, 150, 50])

            # player position
            playerX += playerX_change
            if playerX <= 30:
                playerX = 30
            elif playerX >= 940:
                playerX = 940

            playerY += playerY_change
            if playerY <= 30:
                playerY = 30
            elif playerY >= 530:
                playerY = 530

            # Enemy Movement
            for i in range(num_of_enemies):

                # Game Over
                if enemyY[i] > 400:
                    for j in range(num_of_enemies):
                        enemyY[j] = 100000000000000000000000000 #you can use any value greater than 530
                    game_over_text()
                    break

                # enemy speed
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 2
                    enemyY[i] += 3
                elif enemyX[i] >= 936:
                    enemyX_change[i] = -2
                    enemyY[i] += 3

                # Collision
                collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
                if collision:
                    score_value += 1
                    enemyX[i] = random.randint(0, 936)
                    enemyY[i] = random.randint(50, 150)

                enemy(enemyX[i], enemyY[i], i)

            screen.blit(text, (17, 560))
            screen.blit(text1, (850, 560))

            player(playerX, playerY)
            show_score(textX, testY)
            pygame.display.update()

    # two player
    def twoplayer():
        pygame.init()

        # screen res
        n = (1000, 600)

        # create the screen
        screen = pygame.display.set_mode(n)

        # white and black color
        white = (255, 255, 255)
        black = (0, 0, 0)

        # font
        smallfont = pygame.font.SysFont('bold', 60)
        # adding text
        text = smallfont.render('Home', True, white)
        text1 = smallfont.render('Restart', True, white)

        # Background
        background = pygame.image.load('applegamebgnew.png')

        # adding game title
        pygame.display.set_caption("apple smasher")

        # player one
        playerimg = pygame.image.load('triangle.png')
        playerX = 370
        playerY = 480
        playerX_change = 0
        playerY_change = 0

        # player two
        playerimg1 = pygame.image.load('triangle.png')
        playerX1 = 670
        playerY1 = 480
        playerX_change1 = 0
        playerY_change1 = 0

        # Enemy
        enemyimg = []
        enemyX = []
        enemyY = []
        enemyX_change = []
        enemyY_change = []

        # total number of enemies
        num_of_enemies = 10

        for i in range(num_of_enemies):
            enemyimg.append(pygame.image.load('dot.png'))
            # enemy position
            enemyX.append(random.randint(40, 40))
            enemyY.append(random.randint(40, 40))
            # enemy x-axis distance
            enemyX_change.append(1)
            # enemy y-axis distance
            enemyY_change.append(10)

        # Score
        score_value = 0
        score_value1 = 0
        font = pygame.font.Font('freesansbold.ttf', 32)

        # score position
        scoreX = 10
        scoreY = 10
        scoreX1 = 830
        scoreY1 = 10

        # Game Over
        over_font = pygame.font.Font('freesansbold.ttf', 64)

        def show_score(x, y):
            score = font.render("Score1 : " + str(score_value), True, (255, 255, 255))
            screen.blit(score, (x, y))

        def show_score1(x, y):
            score1 = font.render("Score2 : " + str(score_value1), True, (255, 255, 255))
            screen.blit(score1, (x, y))

        def game_over_text():
            over_text = over_font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(over_text, (300, 250))

        def player(x, y):
            screen.blit(playerimg, (x, y))

        def player1(x, y):
            screen.blit(playerimg1, (x, y))

        def enemy(x, y, i):
            screen.blit(enemyimg[i], (x, y))

        def isCollision(enemyX, enemyY, playerX, playerY):
            distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
            if distance < 27:
                return True
            else:
                return False

        def isCollision1(enemyX, enemyY, playerX1, playerY1):
            distance = math.sqrt(math.pow(enemyX - playerX1, 2) + (math.pow(enemyY - playerY1, 2)))
            if distance < 27:
                return True
            else:
                return False

        # Game Loop
        gameloop = True
        while gameloop:

            # RGB = Red, Green, Blue
            screen.fill((0, 0, 0))
            # Background Image
            screen.blit(background, (0, 0))
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameloop = False

                # if keystroke is pressed check whether its right or left
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        playerY_change = -2
                    elif event.key == pygame.K_s:
                        playerY_change = 2
                    elif event.key == pygame.K_a:
                        playerX_change = -2
                    elif event.key == pygame.K_d:
                        playerX_change = 2
                    elif event.key == pygame.K_UP:
                        playerY_change1 = -2
                    elif event.key == pygame.K_DOWN:
                        playerY_change1 = 2
                    elif event.key == pygame.K_LEFT:
                        playerX_change1 = -2
                    elif event.key == pygame.K_RIGHT:
                        playerX_change1 = 2

                # checks if a mouse is clicked
                if event.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button the game is terminated
                    if 0 <= mouse[0] <= 150 and 550 <= mouse[1] <= 610:
                        game()

                    elif 850 <= mouse[0] <= 1000 and 550 <= mouse[1] <= 610:
                        twoplayer()

            # if mouse is hovered on a button it
            # changes to lighter shade
            # for 1st text
            if 0 <= mouse[0] <= 150 and 550 <= mouse[1] <= 610:
                pygame.draw.rect(screen, black, [0, 550, 150, 50])

            # for 2nd text
            elif 850 <= mouse[0] <= 1000 and 550 <= mouse[1] <= 610:
                pygame.draw.rect(screen, black, [850, 550, 150, 50])

            # player position
            playerX += playerX_change
            if playerX <= 30:
                playerX = 30
            elif playerX >= 940:
                playerX = 940

            playerY += playerY_change
            if playerY <= 30:
                playerY = 30
            elif playerY >= 530:
                playerY = 530

            # 2nd player
            playerX1 += playerX_change1
            if playerX1 <= 30:
                playerX1 = 30
            elif playerX1 >= 940:
                playerX1 = 940

            playerY1 += playerY_change1
            if playerY1 <= 30:
                playerY1 = 30
            elif playerY1 >= 530:
                playerY1 = 530

            # Enemy Movement
            for i in range(num_of_enemies):

                # Game Over
                if enemyY[i] > 440:
                    for j in range(num_of_enemies):
                        enemyY[j] = 100000000000000000000000000
                    game_over_text()
                    break

                # enemy speed
                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 2
                    enemyY[i] += 3
                elif enemyX[i] >= 936:
                    enemyX_change[i] = -2
                    enemyY[i] += 3

                # Collision
                collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)
                if collision:
                    score_value += 1
                    enemyX[i] = random.randint(0, 936)
                    enemyY[i] = random.randint(50, 150)

                enemy(enemyX[i], enemyY[i], i)

                # Collision
                collision1 = isCollision1(enemyX[i], enemyY[i], playerX1, playerY1)
                if collision1:
                    score_value1 += 1
                    enemyX[i] = random.randint(0, 936)
                    enemyY[i] = random.randint(50, 150)

                enemy(enemyX[i], enemyY[i], i)

            screen.blit(text, (17, 560))
            screen.blit(text1, (850, 560))

            player(playerX, playerY)
            player1(playerX1, playerY1)
            show_score(scoreX, scoreY)
            show_score1(scoreX1, scoreY1)
            pygame.display.update()

    while True:

        # first filling bg with black then adding bg image
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

                # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                # if the mouse is clicked on the
                # button the game is terminated
                if 188 <= mouse[0] <= 338 and 188 <= mouse[1] <= 238:
                    oneplayer()

                elif 185 <= mouse[0] <= 335 and 253 <= mouse[1] <= 303:
                    twoplayer()

                elif 160 <= mouse[0] <= 360 and 320 <= mouse[1] <= 370:
                    pygame.quit()

        # if mouse is hovered on a button it
        # changes to lighter shade
        # for 1st text
        if 188 <= mouse[0] <= 338 and 188 <= mouse[1] <= 238:
            pygame.draw.rect(screen, black, [188, 188, 150, 50])

        # for 2nd text
        elif 185 <= mouse[0] <= 335 and 253 <= mouse[1] <= 303:
            pygame.draw.rect(screen, white, [191, 253, 150, 50])

        # for 3rd text
        elif 160 <= mouse[0] <= 360 and 320 <= mouse[1] <= 370:
            pygame.draw.rect(screen, black, [200, 318, 150, 50])

        # add text on the screen
        screen.blit(text, (210, 200))
        screen.blit(text1, (205, 265))
        screen.blit(text2, (240, 330))

        # updates the display of the game
        pygame.display.update()

game()
