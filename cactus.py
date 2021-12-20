import pygame
import os
import random
from decouple import config
from dino import *
from utils import check_speed

pygame.font.init()

STAT_FONT = pygame.font.SysFont("comicsans", 50)

CACTUS_IMGS = [pygame.image.load(os.path.join("images", "LargeCactus1.png")),
               pygame.image.load(os.path.join("images", "LargeCactus2.png")),
               pygame.image.load(os.path.join("images", "LargeCactus3.png")),
               pygame.image.load(os.path.join("images", "SmallCactus1.png")),
               pygame.image.load(os.path.join("images", "SmallCactus2.png")),
               pygame.image.load(os.path.join("images", "SmallCactus3.png"))]

class Cactus:
    VEL = int(config('SPEED'))
    IMGS = CACTUS_IMGS

    check_speed(VEL)

    def __init__(self):
        self.x = 1200
        self.y = 550
        self.passed = False
        self.random_cactus = random.randrange(0, 6)
        self.type = 1

        if(self.random_cactus >= 3):
            self.y = 570

        self.img = self.IMGS[self.random_cactus]

    def move(self) -> None:
        self.x -= self.VEL

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.img, (self.x, self.y))

    def collide(self, dino: Dino) -> bool:
        dino_mask = dino.get_mask()
        cactus_mask = pygame.mask.from_surface(self.img)

        return dino_mask.overlap(cactus_mask, (self.x - dino.x, self.y - dino.y))

