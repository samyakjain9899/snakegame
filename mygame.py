import pygame, sys
import time
import random

pygame.init()

white = (255, 223, 0)
black = (100, 0, 0)
red = (255, 0, 0)
window_width = 800
window_height = 600

gameDisplay = pygame.display.set_mode((window_width, window_height))#set_mode(size=(0, 0), flags=0, depth=0, display=0) -> Surface
#Initialize a window or screen for display
pygame.display.set_caption("slither")#set_caption(title, icontitle=None) 
font = pygame.font.SysFont(None, 25, bold = True)# pygame.font.SysFont(name, size, bold=False, italic=False, constructor=None)
def myquit():
    pygame.quit()
    sys.exit(0)

# part 2
clock = pygame.time.Clock()#create an object to help track time
FPS = 5# frames per second, the screen get refresh 5 times per second
blockSize = 20
noPixel = 0
def snake(blockSize, snakelist): #x = 250 - (segment_width + segment_margin) * i

    for size in snakelist:
        pygame.draw.rect(gameDisplay, black, [size[0] + 5, size[1], blockSize, blockSize], 2)
        #rect(Surface, color, Rect, width=0) -> Rect draw a rectangle shape
def message_to_screen(msg, color):

    screen_text = font.render(msg, True, color)

    gameDisplay.blit(screen_text, [window_width / 2, window_height / 2])

def gameLoop():

    gameExit = False#
    #for exit from the game:

    gameOver = False# when snake crashes

    lead_x = window_width / 2

    lead_y = window_height / 2

    change_pixels_of_x = 0

    change_pixels_of_y = 0

    snakelist = []# initially empty only head and as snake run it fills

    snakeLength = 1

# generates everytime random apple
    randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0

    randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0

# starting game and run it till somebody says exit
    while not gameExit:

    #this loop is to give you multiple lifes
        while gameOver == True: #fill display with white color
            gameDisplay.fill(white)# the message screen show
            message_to_screen("Game over, press c to play again or Q to quit", red)# update screen
            pygame.display.update()

# pick data from event queue
            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    gameOver = False#
#if we quit game will be exited

                    gameExit = True

                if event.type == pygame.KEYDOWN: #q
                #for start again
                    if event.key == pygame.K_q:

                        gameExit = True

                        gameOver = False

                    if event.key == pygame.K_c:

                        gameLoop()
    # logic1 - herewe have quit event and key events

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                gameExit = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    myquit()

                leftArrow = event.key == pygame.K_LEFT

                rightArrow = event.key == pygame.K_RIGHT

                upArrow = event.key == pygame.K_UP

                downArrow = event.key == pygame.K_DOWN

                if leftArrow:

                    change_pixels_of_x = -blockSize

                    change_pixels_of_y = noPixel

                elif rightArrow:

                    change_pixels_of_x = blockSize

                    change_pixels_of_y = noPixel

                elif upArrow:

                    change_pixels_of_y = -blockSize

                    change_pixels_of_x = noPixel

                elif downArrow:

                    change_pixels_of_y = blockSize

                    change_pixels_of_x = noPixel
                    # logic2
            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0: #if snake cross the boundry game over is true
                gameOver = True#
#if not cross we change pixel of x and y
        lead_x += change_pixels_of_x

        lead_y += change_pixels_of_y

        gameDisplay.fill(white)

        AppleThickness = 20

        print([int(randomAppleX), int(randomAppleY), AppleThickness, AppleThickness])

        pygame.draw.rect(gameDisplay, red, [randomAppleX, randomAppleY, AppleThickness, AppleThickness])

        # appending in the list
        allspriteslist = []

        allspriteslist.append(lead_x)

        allspriteslist.append(lead_y)

        snakelist.append(allspriteslist)

#
       # if snake list greator than snake list we delete first part of list
        if len(snakelist) > snakeLength:

            del snakelist[0]

        for eachSegment in snakelist[: -1]:

            if eachSegment == allspriteslist:

                gameOver = True

# drawing snake and update screen
        snake(blockSize, snakelist)

        pygame.display.update()

# logic5 - i eat the appl and increase snake length to 1
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:

            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:

                randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0

                randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0

                snakeLength += 1

        clock.tick(FPS)

    pygame.quit()

    quit()

gameLoop()
#The start argument is the starting number in a random range. i.e., lower limit. The default value of start is 0 if not specified.
#The stop argument is the last number in a random range. the stop argument is the upper limit.
#The step is a difference between each number in the sequence. The step is optional parameters. The default value of the step is 1 if not specified