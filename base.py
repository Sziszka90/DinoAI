import pygame
import os

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "Track.png")))

class Base:
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self,velocity):
        self.y = 620
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

