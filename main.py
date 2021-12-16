import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import neat
import time
import random
pygame.font.init()

WIN_WIDTH = 1200
WIN_HEIGHT = 700

DINO_IMGS = [pygame.image.load(os.path.join("images", "DinoJump.png")),
             pygame.image.load(os.path.join("images", "DinoRun1.png")),
             pygame.image.load(os.path.join("images", "DinoRun2.png"))]

CACTUS_IMGS = [pygame.image.load(os.path.join("images", "LargeCactus1.png")),
            pygame.image.load(os.path.join("images", "LargeCactus2.png")),
            pygame.image.load(os.path.join("images", "LargeCactus3.png")),
            pygame.image.load(os.path.join("images", "SmallCactus1.png")),
            pygame.image.load(os.path.join("images", "SmallCactus2.png")),
            pygame.image.load(os.path.join("images", "SmallCactus3.png"))]

BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("images", "Track.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)

class Dino:
    IMGS = DINO_IMGS
    ANIMATION_TIME = 5
    JUMP_TIME = 20

    def __init__(self):
        self.tick_count = 0
        self.img = self.IMGS[0]
        self.x = 400
        self.y = 550
        self.height = 10
        self.jump_flag = False
        self.img_count_run = 0
        self.img_count_jump = 0

    def jump_motion(self, win):
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
                
            win.blit(self.img, (self.x, self.y))
    
    def run_motion(self,win):
        if(not self.jump_flag):
            self.img_count_run += 1

            if self.img_count_run < self.ANIMATION_TIME:
                self.img = self.IMGS[1]
            elif self.img_count_run < self.ANIMATION_TIME*2:
                self.img = self.IMGS[2]
            elif self.img_count_run > self.ANIMATION_TIME*2:  
                self.img_count_run = 0
            
            win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

#-------------------------------------------------------------------------------

class Base:
    VEL = 10
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self):
        self.y = 620
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

class Cactus:
    VEL = 10

    def __init__(self):
        self.x = 1200
        self.y = 550
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.passed = False
        self.random_num = random.randrange(0,6)

        if(self.random_num>=3):
            self.y = 570

        self.cactus_img = CACTUS_IMGS[self.random_num]

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.cactus_img, (self.x, self.y))

    def collide(self, dino):
        dino_mask = dino.get_mask()
        cactus_mask = pygame.mask.from_surface(self.cactus_img)

        if (dino_mask.overlap(cactus_mask, (self.x - dino.x, self.y - dino.y))):
            print("COLLIDE")

        return dino_mask.overlap(cactus_mask, (self.x - dino.x, self.y - dino.y))
        
        


dino = Dino()
base = Base()
cactuses = []
cactuses.append(Cactus())
        
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

color = (255,255,255)
win.fill(color)
pygame.display.update()

clock = pygame.time.Clock()

pygame.display.update()

run = True

add_cactus = False

while run:
    clock.tick(30)

    win.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jump_flag = True

    dino.run_motion(win)
    dino.jump_motion(win)
    base.draw(win)
    base.move()

    for cactus in cactuses:
        if cactus.x == dino.x:
            add_cactus = True

        if cactus.x < 0:
            cactuses.remove(cactus)

        cactus.draw(win)
        cactus.move()
        cactus.collide(dino)

    if (add_cactus):
        cactuses.append(Cactus())
        add_cactus = False

    pygame.display.update()


        


