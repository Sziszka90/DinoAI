import pygame
import os
from decouple import config as get_env_var

BG_IMG = pygame.image.load(os.path.join("images", "background.png"))

class Background:
    WIDTH = BG_IMG.get_width()
    IMG = BG_IMG

    def __init__(self, VEL):
        self.y = 0
        self.x1 = 0
        self.x2 = self.WIDTH
        self.VEL = VEL

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