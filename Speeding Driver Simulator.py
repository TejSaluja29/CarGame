import pygame, sys, random

pygame.init()  # initialize pygame

clock = pygame.time.Clock()
FPS = 120  # set fps

w = 1500
h = 750
windowSize = w, h
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('speeding driver simulator')

bg_image = pygame.image.load('car_bg.png').convert_alpha()

# setting starting x and y values for road rectangles and height and width
rectStartx1 = w / 5
rectStartx2 = w / 5 + rectStartx1
rectStartx3 = w / 5 + (rectStartx1 * 2)
rectStartx4 = w / 5 + (rectStartx1 * 3)
rectStarty1 = 100
rectStarty2 = 300
rectStarty3 = 500
rectStarty4 = 700
rectStarty5 = 900
rectWidth = 20
rectHeight = 80

rectSpeed = 12  # Speed of dropping rectangle
carSpeed = 7
# Colour
red = (255, 0, 0)
gray = (40, 40, 40)
light_gray = (70, 70, 70)
white = (255, 255, 255)
light_blue = (0, 170, 255)

# Player Rectangle
car = pygame.image.load('car_player.png')
carSize = car.get_size()
carW = carSize[0]
carH = carSize[1]
x = w / 2 - carW / 2 + 10  # 474
y = h - (carH + 100)  # 500

obsXpos = random.choice([x, 720, 130])
obsYpos = -300

obsImage = random.choice(['car_blue.png', 'car_pink.png', 'car_green.png', 'car_yellow.png', 'car_police.png'])
obsCar = pygame.image.load(obsImage)
coinImage = pygame.image.load('coin.png')

obstacles = []
coins = []
score = 0


def sound():
    crashSound = pygame.mixer.Sound('crash.wav')

    return crashSound


def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (w, h))
    screen.blit(scaled_bg, (0, 0))


# Generate Rectangles Function
def generateRect(x1, y1, w1, h1, colour):
    return pygame.draw.rect(screen, colour, [x1, y1, w1, h1])


def road():
    # global each variable
    global rectStartx1
    global rectStartx2
    global rectStartx3
    global rectStartx4
    global rectStarty1
    global rectStarty2
    global rectStarty3
    global rectStarty4
    global rectStarty5

    # generate each rectangle with the previously defined x,y coordinates and width and hieght and color
    generateRect(rectStartx1, rectStarty1, rectWidth, rectHeight, white)
    generateRect(rectStartx2, rectStarty1, rectWidth, rectHeight, white)
    generateRect(rectStartx3, rectStarty1, rectWidth, rectHeight, white)
    generateRect(rectStartx4, rectStarty1, rectWidth, rectHeight, white)
    generateRect(rectStartx1, rectStarty2, rectWidth, rectHeight, white)
    generateRect(rectStartx2, rectStarty2, rectWidth, rectHeight, white)
    generateRect(rectStartx3, rectStarty2, rectWidth, rectHeight, white)
    generateRect(rectStartx4, rectStarty2, rectWidth, rectHeight, white)
    generateRect(rectStartx1, rectStarty3, rectWidth, rectHeight, white)
    generateRect(rectStartx2, rectStarty3, rectWidth, rectHeight, white)
    generateRect(rectStartx3, rectStarty3, rectWidth, rectHeight, white)
    generateRect(rectStartx4, rectStarty3, rectWidth, rectHeight, white)
    generateRect(rectStartx1, rectStarty4, rectWidth, rectHeight, white)
    generateRect(rectStartx2, rectStarty4, rectWidth, rectHeight, white)
    generateRect(rectStartx3, rectStarty4, rectWidth, rectHeight, white)
    generateRect(rectStartx4, rectStarty4, rectWidth, rectHeight, white)
    generateRect(rectStartx1, rectStarty5, rectWidth, rectHeight, white)
    generateRect(rectStartx2, rectStarty5, rectWidth, rectHeight, white)
    generateRect(rectStartx3, rectStarty5, rectWidth, rectHeight, white)
    generateRect(rectStartx4, rectStarty5, rectWidth, rectHeight, white)

    rectStarty1 += rectSpeed  # Move rectangles down the screen
    rectStarty2 += rectSpeed
    rectStarty3 += rectSpeed
    rectStarty4 += rectSpeed
    rectStarty5 += rectSpeed

    if rectStarty1 > h:  # Check to see when rectangle is off the screen
        rectStarty1 = 0 - rectHeight  # draw another rectangle with this Y co-ordinate
    if rectStarty2 > h:
        rectStarty2 = 0 - rectHeight
    if rectStarty3 > h:
        rectStarty3 = 0 - rectHeight
    if rectStarty4 > h:
        rectStarty4 = 0 - rectHeight
    if rectStarty5 > h:
        rectStarty5 = 0 - rectHeight


def create_obstacle():
    global obsXpos
    global obsYpos

    obsImage = random.choice(['car_blue.png', 'car_pink.png', 'car_green.png', 'car_yellow.png', 'car_police.png'])
    obsCar = pygame.image.load(obsImage)
    obsCarSize = obsCar.get_size()
    obsW = obsCarSize[0]
    obsH = obsCarSize[1]

    obsXpos = random.randint(40, w - obsW - 40)
    obsYpos = -obsH

    return pygame.Rect(obsXpos, obsYpos, obsW, obsH)  # Create a rectangle object for the obstacle


def create_coins():
    global coinXpos
    global coinYpos

    coinSize = coinImage.get_size()
    coinW = coinSize[0]
    coinH = coinSize[1]

    coinXpos = random.randint(40, w - coinW - 40)
    coinYpos = -coinH

    return pygame.Rect(coinXpos, coinYpos, coinW, coinH)  # Create a rectangle object for the obstacle


def top_display(count):
    # create the display for difficulty settings and score
    font1 = pygame.font.Font('Pixeltype.ttf', 50)
    font2 = pygame.font.Font('Pixeltype.ttf', 42)
    scoreFont = font1.render("Score: " + str(count), True, white)
    instructions = font2.render("h  =  hard mode , m  =  medium mode , e  =  easy mode", True, white)
    screen.blit(scoreFont, (w - 225, 15))
    screen.blit(instructions, (50, 17))


def game_over():
    # create the game over screen

    font1 = pygame.font.Font('Pixeltype.ttf', 175)
    font2 = pygame.font.Font('Pixeltype.ttf', 58)
    gameoverFont = font1.render('Game Over!!', True, red)
    restartFont = font2.render('press space to restart', True, red)
    gameOverSize = gameoverFont.get_size()
    restartFontSize = restartFont.get_size()
    screen.blit(gameoverFont, (w / 2 - gameOverSize[0] / 2 + 25, h / 2))
    screen.blit(restartFont, (w / 2 - restartFontSize[0] / 2 + 25, h / 2 + gameOverSize[1]))


def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)


game_over_text_shown = False  # to control when the game over text is on the screen
allow_movement = True  # to control car movement after game over


def gameloop():
    global allow_movement, x, y, rectSpeed, carSpeed, game_over_text_shown, score, event, FPS

    pygame.mixer.init()
    pygame.mixer.music.load('gameSound.mp3')  # Load the game sound file
    pygame.mixer.music.play(-1)  # play infinitely
    crash = sound()
    crash_sound_played = False

    obsImage = random.choice(['car_blue.png', 'car_pink.png', 'car_green.png', 'car_yellow.png', 'car_police.png'])
    obsCar = pygame.image.load(obsImage)

    running = True
    game_over_text_shown = False
    allow_movement = True
    rectSpeed = 12
    carSpeed = 7

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # if the movement is allowed then itll take the input from the keyboard
        if allow_movement:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                x += 5
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                x -= 5
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                y -= 2
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                y += 5
            if keys[pygame.K_e]:
                carSpeed = 3
            if keys[pygame.K_m]:
                carSpeed = 7
            if keys[pygame.K_h]:
                carSpeed = 10
        # set boundaries
        if x + carW > w - 40:
            x = w - carW - 40
        if y + carH > h:
            y = h - carH
        if x <= 40:
            x = 40
        if y <= 60:
            y = 60

        screen.fill(gray)
        road()  # make the road

        if len(obstacles) < 5:  # limit the munber of cars on the screen to 5
            if random.random() < 0.05:  # generate a random number to make the probability of the obsCar being made to 5%
                obstacle = create_obstacle()
                for existing_obstacle in obstacles:
                    if check_collision(obstacle,
                                       existing_obstacle):  # check if there is already a car in the list with the same coordinates
                        break
                else:
                    for coin in coins:
                        if check_collision(obstacle,
                                           coin):  # check if there is already a coin in the list with the same coordinates
                            break
                    else:
                        obstacles.append(obstacle)

        for obstacle in obstacles:
            obstacle.y += carSpeed  # make the cars y coordinate move down the screen
            if obstacle.y > h:
                obstacles.remove(obstacle)
            screen.blit(obsCar, obstacle)

            if obstacle.colliderect(pygame.Rect(x, y, carW, carH)):
                if not crash_sound_played:
                    pygame.mixer.music.stop()  # stops backgroud music
                    crash.play()  # plays crash sound
                    crash.set_volume(1)
                    crash_sound_played = True
                # stops eveything from moving
                rectSpeed = 0
                carSpeed = 0
                allow_movement = False
                game_over_text_shown = True
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    coins.clear()
                    obstacles.clear()
                    score = 0
                    running = False
                    intro()  # restarts when the space bar is pressed

        if len(coins) < 2:  # makes sure theres only 2 coins on the screen at once
            if random.random() < 0.05:  # makes the probability of a coin spawning 5%
                coin = create_coins()
                # checks to make sure the new generated coin does collide with any existing coins or obstacles
                for existing_coin in coins:
                    if check_collision(coin, existing_coin):
                        break
                else:
                    for obstacle in obstacles:
                        if check_collision(coin, obstacle):
                            break
                    else:
                        coins.append(coin)

        for coin in coins:
            coin.y += carSpeed  # move coin down the screen
            if coin.y > h:
                coins.remove(coin)
            screen.blit(coinImage, coin)  # blit coin to screen

            if coin.colliderect(
                    pygame.Rect(x, y, carW, carH)):  # if the players car collides with a coin, then they score a point
                score += 1
                coins.remove(coin)

        # creates borders, and top screen display
        pygame.draw.rect(screen, light_gray, (0, 0, 40, h))
        pygame.draw.rect(screen, light_gray, (w - 40, 0, 40, h))
        pygame.draw.rect(screen, light_gray, (0, 0, w, 60))
        top_display(score)
        screen.blit(car, (x, y))

        if game_over_text_shown:
            game_over()
        pygame.display.update()
        clock.tick(FPS)
    sys.exit()  # exits when loop stops


def intro():
    intro = True

    while intro:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if keys[pygame.K_SPACE]:  # space bar starts the game and ends intro screen
                intro = False
                gameloop()
            draw_bg()
            # name of the game and instructions to play and how to start
            font1 = pygame.font.Font("Pixeltype.ttf", 175)
            font2 = pygame.font.Font("Pixeltype.ttf", 72)
            title = font1.render("Speeding driver simulator", True, red)
            titleSize = title.get_size()
            instructions1 = font2.render('WASD or Arrow Keys to move', True, red)  #
            instructions2 = font2.render('Collect the coins and Avoid the other cars!!', True, red)
            instructions3 = font2.render('PRESS SPACE TO START', True, (0, 0, 255))
            instructionsSize1 = instructions1.get_size()
            instructionsSize2 = instructions2.get_size()
            instructionsSize3 = instructions3.get_size()
            screen.blit(title, (w / 2 - titleSize[0] / 2, 100))
            screen.blit(instructions1, (w / 2 - instructionsSize1[0] / 2, 250))
            screen.blit(instructions2, (w / 2 - instructionsSize2[0] / 2, 300))
            screen.blit(instructions3, (w / 2 - instructionsSize3[0] / 2, 500))
            pygame.display.update()


intro()
