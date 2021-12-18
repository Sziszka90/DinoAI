import random
import time
import neat
import pygame
import os
from cactus import *
from base import *
from dino import *
from draw import *

WIN_WIDTH = 1200
WIN_HEIGHT = 700

def main(genomes: neat.DefaultGenome, config: neat.Config) -> None:
    nets = []
    ge = []
    dinos = []
    base = Base()
    cactuses = [Cactus()]
    background = Background()

    score = 0
    
    for _, g in genomes: 
        net = neat.nn.FeedForwardNetwork.create(g, config) 
        nets.append(net) 
        dinos.append(Dino())
        g.fitness = 0 
        ge.append(g)

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
        cactus_ind = 0

        if len(dinos) > 0:
            if len(cactuses) > 1 and dinos[0].x > cactuses[0].x + cactuses[0].cactus_img.get_width():
                cactus_ind = 1
        else:
            run = False
            break

        for x, dino in enumerate(dinos):
            dino.motion(win)
            ge[x].fitness += 0.1

            output = nets[x].activate((dino.x + dino.img.get_width(), cactuses[cactus_ind].x))

            if output[0] > 0.5:
                dino.jump()

        add_cactus = False
        rem = []
        for cactus in cactuses:
            for x, dino in enumerate(dinos):
                if cactus.collide(dino):
                    ge[x].fitness -= 1
                    dinos.pop(x)
                    nets.pop(x)
                    ge.pop(x)
            
                if not cactus.passed and cactus.x < dino.x:
                    cactus.passed = True

            if cactus.x + cactus.cactus_img.get_width() < 0:
                rem.append(cactus)
            
            if (cactus.x == dino.x):
                score += 1

            cactus.move()
            
            if cactus.passed:
                for g in ge:
                    g.fitness += 5

        adding_cactus(cactuses)
        
        for r in rem:
            cactuses.remove(r)

        background.move()
        base.move()
        draw_window(win, background, dinos, cactuses, base, score)

def run(config_path: os.path) -> None:
    config = neat.config.Config(neat.DefaultGenome,            
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, 
                                neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main,50) 
                
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__) 
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path) 
