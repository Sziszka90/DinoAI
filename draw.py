import random
import pygame
from cactus import *
from bird import *
from dino import *
from base import *
from background import *

STAT_FONT = pygame.font.SysFont("comicsans", 50)

cactus_tick = 0
bird_tick = 0
generate_random_num = False
random_num = 0
random_obstacle = 0

def adding_obstacle(obstacles: list) -> None:
    VEL = int(config('SPEED'))

    global random_obstacle
    global cactus_tick
    global bird_tick
    global generate_random_num
    global random_num
    global random_bird_height

    rand_range = []
    rand_range.append(round((50/VEL)*10))    
    rand_range.append(round((100/VEL)*10))

    if (not generate_random_num):
        random_num = random.randrange(rand_range[0], rand_range[1])
        random_bird_height = random.randrange(0,2)
        random_obstacle = random.randrange(0,2)
        generate_random_num = True

    if(random_obstacle == 0) and generate_random_num:
        cactus_tick += 1

        if (cactus_tick == random_num):
            obstacles.append(Cactus())
            generate_random_num = False
            cactus_tick = 0
    elif(random_obstacle == 1) and generate_random_num:
        bird_tick += 1

        if (bird_tick == random_num):
            if(random_bird_height == 0):
                obstacles.append(Bird(550))
            elif(random_bird_height == 1):
                obstacles.append(Bird(490))
            generate_random_num = False
            bird_tick = 0

def reset_adding_obstacle():
    global cactus_tick
    global bird_tick
    global generate_random_num

    generate_random_num = False
    cactus_tick = 0
    bird_tick = 0

def draw_window(win: pygame.Surface, background: Background, dinos: Dino, obstacles: list, base: Base, status: dict) -> None:
    background.draw(win)

    text = STAT_FONT.render("Score: " + str(status["score"]),1,(0,0,0))
    win.blit(text,(10, 10))

    text = STAT_FONT.render("Running generation: " + str(status["generation"]),1,(0,0,0))
    win.blit(text,(10, 45))

    text = STAT_FONT.render("Population size: " + str(status["population_size"]),1,(0,0,0))
    win.blit(text,(10, 80))

    base.draw(win)

    for dino in dinos:
        dino.draw(win)

    for obstacle in obstacles:
        obstacle.draw(win)

    pygame.display.set_caption('Mozilla Dino AI')

    pygame.display.update()

