import pygame
import os
from decouple import config as get_env_var
from dino import *

pygame.font.init()

STAT_FONT = pygame.font.SysFont("comicsans", 50)

BIRD_IMGS = [pygame.image.load(os.path.join("images", "bird_1.png")),
               pygame.image.load(os.path.join("images", "bird_2.png"))]

class Bird:
    ANIMATION_TIME = 5
    IMGS = BIRD_IMGS

    def __init__(self, y, VEL):
        self.x = 1200
        self.y = y
        self.passed = False
        self.img_count_bird = 0
        self.img = self.IMGS[0]
        self.VEL = VEL

    def move(self) -> None:
        self.x -= self.VEL

        self.img_count_bird += 1

        if self.img_count_bird < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count_bird < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count_bird > self.ANIMATION_TIME*2:
            self.img_count_bird = 0

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.img, (self.x, self.y))

    def collide(self, dino: Dino) -> bool:
        dino_mask = dino.get_mask()
        bird_mask = pygame.mask.from_surface(self.img)

        return dino_mask.overlap(bird_mask, (self.x - dino.x, self.y - dino.y))

