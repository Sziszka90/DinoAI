import pygame
import os
from decouple import config
from utils import check_speed

BG_IMG = pygame.image.load(os.path.join("images", "background.png"))

class Background:

    VEL = int(config('SPEED'))

    check_speed(VEL)

    WIDTH = BG_IMG.get_width()
    IMG = BG_IMG

    def __init__(self):
        self.y = 0
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self) -> None:
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))