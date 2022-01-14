import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import helpers


images = helpers.get_images('track')
helpers.check_images(images)

TRACK_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('resources/images', images[0])))
WIDTH = TRACK_IMG.get_width()

class Track:
    def __init__(self,velocity):
        self.IMG = TRACK_IMG
        self.WIDTH = WIDTH
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

