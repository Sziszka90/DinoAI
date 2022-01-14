import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import helpers


images = helpers.get_images('dino')
helpers.check_images(images)

DINO_IMGS = tuple([pygame.image.load(os.path.join('resources/images', img)) for img in images])
ANIMATION_TIME = 5


class Dino:
    def __init__(self):
        self.IMGS = DINO_IMGS
        self.img = self.IMGS[0]
        self.ANIMATION_TIME = ANIMATION_TIME
        self.x = 400
        self.y = 550
        self.jump = False
        self.down = False
        self.dead = False
        self.tick_count = 0
        self.img_count_run = 0
        self.img_count_jump = 0
        self.img_count_down = 0
        self.img_count_dead = 0

    def motion(self) -> None:
        if(self.jump):
            self.img_count_jump += 1

            if self.img_count_jump < 15:
                self.img = self.IMGS[0]

            if(self.img_count_jump <= 3):
                self.y -= 50
            elif(self.img_count_jump >= 3 and self.img_count_jump < 12):
                pass
            else:
                self.y += 50
                if(self.y >= 550):
                    self.y = 550
                    self.img_count_jump = 0
                    self.jump = False
    
        elif(self.down):
            self.img_count_down += 1

            self.y = 580

            if self.img_count_down < self.ANIMATION_TIME:
                self.img = self.IMGS[3]
            elif self.img_count_down < self.ANIMATION_TIME*2:
                self.img = self.IMGS[4]
            elif self.img_count_down > self.ANIMATION_TIME*2:
                self.img_count_down = 0
                self.down = False

        elif(self.dead):
            self.img_count_dead += 1
            self.y = 550
            self.img = self.IMGS[5]
            self.img_count_dead = 0
            self.dead = False

        else:
            self.img_count_run += 1

            self.y = 550

            if self.img_count_run < self.ANIMATION_TIME:
                self.img = self.IMGS[1]
            elif self.img_count_run < self.ANIMATION_TIME*2:
                self.img = self.IMGS[2]
            elif self.img_count_run > self.ANIMATION_TIME*2:
                self.img_count_run = 0

    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.img, (self.x, self.y))

    def get_mask(self) -> pygame.mask.Mask:
        return pygame.mask.from_surface(self.img)
