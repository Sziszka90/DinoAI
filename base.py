import pygame
import os
from decouple import config as get_env_var
from utils import check_speed

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "Track.png")))

class Base:
    VEL = int(get_env_var('SPEED'))
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    check_speed(VEL)

    def __init__(self):
        self.y = 620
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

