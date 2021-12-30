import pygame
import os

BG_IMG = pygame.image.load(os.path.join("images", "background.png"))

class Background:
    WIDTH = BG_IMG.get_width()
    IMG = BG_IMG

    def __init__(self, velocity):
        self.y = 0
        self.x1 = 0
        self.x2 = self.WIDTH
        self.velocity = velocity

    def move(self) -> None:
        self.x1 -= self.velocity
        self.x2 -= self.velocity

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))