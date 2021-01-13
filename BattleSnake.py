import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

#COLORS
orangecolor = (255, 123, 7)
blackcolor = (0, 0, 0)
redcolor = (213, 50, 80)
greencolor = (0, 255, 0)
bluecolor = (50, 153, 213)


display_width = 400
display_height = 500
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Battlesnake') 
snakeBlock = 10
snakeList = []
snakeSpeed = 15


def structureSnake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, redcolor, [x[0], x[1], snakeBlock, snakeBlock])


def game():
    game_over = False
    game_end = False
    
    x1 = display_width / 2
    y1 = display_height / 2
    
    x1_change = 0
    y1_change = 0

    
    snakeList = []
    length_of_snake = 1



    foodx = round(random.randrange(0,display_width-snakeBlock)/10.0) * 10.0
    foody = round(random.randrange(0,display_height-snakeBlock)/10.0) * 10.0

    while not game_over:
        while game_end == True:
            
            score = length_of_snake - 1
            score_font = pygame.font.SysFont("Times New Roman",35)
            value = score_font.render("Your Score: " + str(score), True, orangecolor)
            dis.blit(value, [display_width / 3, display_height / 5])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over =True
                    game_end = False 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snakeBlock
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snakeBlock
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_end = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blackcolor)
        pygame.draw.rect(dis,bluecolor,[foodx,foody,snakeBlock,snakeBlock])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snakeList.append(snake_Head)


        if len(snakeList) > length_of_snake:
            del snakeList[0]
    

        for x in snakeList[:-1]:
            if x == snake_Head:
                game_end = True

        structureSnake(snakeBlock,snakeList)
        pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width-snakeBlock)/10.0) * 10.0
            foody = round(random.randrange(0, display_height - snakeBlock)/10.0)* 10.0
            length_of_snake += 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

game()
