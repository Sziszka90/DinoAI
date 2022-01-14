from __future__ import annotations
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import random
import pygame
from obstacles import Bird, Cactus


pygame.font.init()
STAT_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)


class Draw:
    def __init__(self, velocity):
        self.cactus_tick = 0
        self.bird_tick = 0
        self.generate_random_num = False
        self.random_num = 0
        self.random_obstacle = 0
        self.random_bird_height = 0
        self.velocity = velocity

    def adding_obstacle(self, obstacles: list) -> None:
        rand_range = []
        rand_range.append(round((50/self.velocity)*10))    
        rand_range.append(round((100/self.velocity)*10))

        if (not self.generate_random_num):
            self.random_num = random.randrange(rand_range[0], rand_range[1])
            self.random_bird_height = random.randrange(0,2)
            self.random_obstacle = random.randrange(0,2)
            self.generate_random_num = True

        if(self.random_obstacle == 0) and self.generate_random_num:
            self.cactus_tick += 1

            if (self.cactus_tick == self.random_num):
                obstacles.append(Cactus(self.velocity))
                self.generate_random_num = False
                self.cactus_tick = 0
        elif(self.random_obstacle == 1) and self.generate_random_num:
            self.bird_tick += 1

            if (self.bird_tick == self.random_num):
                if(self.random_bird_height == 0):
                    obstacles.append(Bird('down',self.velocity))
                elif(self.random_bird_height == 1):
                    obstacles.append(Bird('up',self.velocity))
                self.generate_random_num = False
                self.bird_tick = 0

    def reset_adding_obstacle(self) -> None:
        self.generate_random_num = False
        self.cactus_tick = 0
        self.bird_tick = 0

    def draw_window(self, win: pygame.Surface, background: 'Background', dinos: list, obstacles: list, base: 'Track', status: dict, start: bool, gameover: bool=False) -> None:
        background.draw(win)

        state_pos_y = 10

        for state in status.keys():
            text = STAT_FONT.render(state + str(status[state]),1,(0,0,0))
            win.blit(text,(10, state_pos_y))
            state_pos_y += 35

        base.draw(win)

        for dino in dinos:
            dino.draw(win)

        for obstacle in obstacles:
            obstacle.draw(win)

        if(gameover):
            text = TITLE_FONT.render('GAME OVER!',1,(0,0,0))
            win.blit(text,(460, 250))

        if(not start):
            text = TITLE_FONT.render('Press SPACE to start',1,(0,0,0))
            win.blit(text,(380, 300))

        pygame.display.set_caption('Dino AI')

        pygame.display.update()
