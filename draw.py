import random
import pygame
from cactus import *
from dino import *
from base import *
from background import *
import sys

STAT_FONT = pygame.font.SysFont("comicsans", 50)

cactus_tick = 0
generate_random_num = False
random_num = 0

def adding_cactus(cactuses: list) -> None:
    global cactus_tick
    cactus_tick += 1

    global generate_random_num
    global random_num

    VEL = int(config('SPEED'))
    rand_range = []
    rand_range.append(round((50/VEL)*10))       
    rand_range.append(round((100/VEL)*10))

    if (not generate_random_num):
        random_num = random.randrange(rand_range[0], rand_range[1])
        generate_random_num = True

    if (cactus_tick == random_num):
        cactuses.append(Cactus())
        generate_random_num = False
        cactus_tick = 0

def draw_window(win: pygame.Surface, background: Background, dinos: Dino, cactuses: list, base: Base, score: int) -> None:
    background.draw(win)

    for cactus in cactuses:
        cactus.draw(win)

    text = STAT_FONT.render("Score: " + str(score),1,(0,0,0))
    win.blit(text,(10, 10))

    base.draw(win)

    for dino in dinos:
        dino.draw(win)

    pygame.display.set_caption('Mozilla Dino AI')

    pygame.display.update()

