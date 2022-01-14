from __future__ import annotations
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import random
import pygame
import helpers


images_cactus = helpers.get_images('cactus')
images_bird = helpers.get_images('bird')

helpers.check_images(images_cactus)
helpers.check_images(images_bird)

CACTUS_IMGS = tuple([pygame.image.load(os.path.join('resources/images', img)) for img in images_cactus])
BIRD_IMGS = tuple([pygame.transform.scale(pygame.image.load(os.path.join('resources/images', img)),(100,100)) for img in images_bird])
ANIMATION_TIME = 5


class Cactus:
    def __init__(self, velocity):
        self.IMGS = CACTUS_IMGS
        self.x = 1200
        self.y = 550
        self.passed = False
        self.random_cactus = random.randrange(0, 6)
        self.velocity = velocity

        if(self.random_cactus >= 3):
            self.y = 570

        self.img = self.IMGS[self.random_cactus]

    def move(self) -> None:
        self.x -= self.velocity

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.img, (self.x, self.y))

    def collide(self, dino: 'Dino') -> bool:
        dino_mask = dino.get_mask()
        cactus_mask = pygame.mask.from_surface(self.img)

        return dino_mask.overlap(cactus_mask, (self.x - dino.x, self.y - dino.y))


class Bird:
    def __init__(self, pos, velocity):
        self.IMGS = BIRD_IMGS
        self.img = self.IMGS[0]
        self.ANIMATION_TIME = ANIMATION_TIME
        self.x = 1200
        self.y = 480 if pos == 'up' else 550
        self.passed = False
        self.img_count_bird = 0
        self.velocity = velocity

    def move(self) -> None:
        self.x -= self.velocity

        self.img_count_bird += 1

        if self.img_count_bird < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count_bird < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count_bird > self.ANIMATION_TIME*2:
            self.img_count_bird = 0

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.img, (self.x, self.y))

    def collide(self, dino: 'Dino') -> bool:
        dino_mask = dino.get_mask()
        bird_mask = pygame.mask.from_surface(self.img)

        return dino_mask.overlap(bird_mask, (self.x - dino.x, self.y - dino.y))


