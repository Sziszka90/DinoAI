import random
import pygame
from cactus import *
from bird import *
from dino import *
from base import *
from background import *

STAT_FONT = pygame.font.SysFont("comicsans", 50)

class Draw:
    def __init__(self, VEL):
        self.cactus_tick = 0
        self.bird_tick = 0
        self.generate_random_num = False
        self.random_num = 0
        self.random_obstacle = 0
        self.random_bird_height = 0
        self.VEL = VEL

    def adding_obstacle(self, obstacles: list) -> None:
        rand_range = []
        rand_range.append(round((50/self.VEL)*10))    
        rand_range.append(round((100/self.VEL)*10))

        if (not self.generate_random_num):
            self.random_num = random.randrange(rand_range[0], rand_range[1])
            self.random_bird_height = random.randrange(0,2)
            self.random_obstacle = random.randrange(0,2)
            self.generate_random_num = True

        if(self.random_obstacle == 0) and self.generate_random_num:
            self.cactus_tick += 1

            if (self.cactus_tick == self.random_num):
                obstacles.append(Cactus(self.VEL))
                self.generate_random_num = False
                self.cactus_tick = 0
        elif(self.random_obstacle == 1) and self.generate_random_num:
            self.bird_tick += 1

            if (self.bird_tick == self.random_num):
                if(self.random_bird_height == 0):
                    obstacles.append(Bird(550,self.VEL))
                elif(self.random_bird_height == 1):
                    obstacles.append(Bird(490,self.VEL))
                self.generate_random_num = False
                self.bird_tick = 0

    def reset_adding_obstacle(self) -> None:
        self.generate_random_num = False
        self.cactus_tick = 0
        self.bird_tick = 0

    def draw_window(self, win: pygame.Surface, background: Background, dinos: Dino, obstacles: list, base: Base, status: dict) -> None:
        background.draw(win)

        state_pos_y = 10

        for state in status:
            text = STAT_FONT.render(state + str(status[state]),1,(0,0,0))
            win.blit(text,(10, state_pos_y))
            state_pos_y += 35

        base.draw(win)

        for dino in dinos:
            dino.draw(win)

        for obstacle in obstacles:
            obstacle.draw(win)

        pygame.display.set_caption('Mozilla Dino AI')

        pygame.display.update()

