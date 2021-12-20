import pygame
import os

DINO_IMGS = [pygame.image.load(os.path.join("images", "DinoJump.png")),
             pygame.image.load(os.path.join("images", "DinoRun1.png")),
             pygame.image.load(os.path.join("images", "DinoRun2.png")),
             pygame.image.load(os.path.join("images", "dino_down_1.png")),
             pygame.image.load(os.path.join("images", "dino_down_2.png"))]

class Dino:
    IMGS = DINO_IMGS
    ANIMATION_TIME = 5
    JUMP_TIME = 15

    def __init__(self):
        self.tick_count = 0
        self.img = self.IMGS[0]
        self.x = 400
        self.y = 550
        self.jump_flag = False
        self.down_flag = False
        self.img_count_run = 0
        self.img_count_jump = 0
        self.img_count_down = 0

    def jump(self) -> None:
        self.jump_flag = True

    def down(self) -> None:
        self.down_flag = True

    def motion(self) -> None:
        if(self.jump_flag):
            self.img_count_jump += 1

            if self.img_count_jump < self.JUMP_TIME:
                self.img = self.IMGS[0]

            if(self.img_count_jump < self.JUMP_TIME/2):
                self.y -= 20
            else:
                self.y += 10
                if(self.y == 550):
                    self.img_count_jump = 0
                    self.jump_flag = False
    
        elif(self.down_flag):
            self.img_count_down += 1

            self.y = 580

            if self.img_count_down < self.ANIMATION_TIME:
                self.img = self.IMGS[3]
            elif self.img_count_down < self.ANIMATION_TIME*2:
                self.img = self.IMGS[4]
            elif self.img_count_down > self.ANIMATION_TIME*2:
                self.img_count_down = 0
                self.down_flag = False
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