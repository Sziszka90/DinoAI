import neat
import pygame
import os
from cactus import *
from base import *
from dino import *
from draw import *
from utils import direction
from decouple import config

WIN_WIDTH = 1200
WIN_HEIGHT = 700

generation = 0

def main(genomes: neat.DefaultGenome, config: neat.Config) -> None:
    nets = []
    ge = []
    dinos = []
    base = Base()
    obstacles = [Bird()]
    background = Background()
    reset_adding_obstacle()

    score = 0
    global generation
    generation += 1
    population_size = 0
    status = {}
    
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
                
        obstacle_ind = 0
        
        if len(dinos) > 0:
            if ((len(obstacles) > 1) and (dinos[0].x > obstacles[0].x + obstacles[0].img.get_width())):
                obstacle_ind = 1
        else:
            run = False
            break
        
        for x, dino in enumerate(dinos):
            output = nets[x].activate(direction(dino, obstacles, obstacle_ind))

            if(type(obstacles[obstacle_ind]) == type(Bird())):
                if output[0] > 0.5:
                    dino.down()
            elif(type(obstacles[obstacle_ind]) == type(Cactus())):
                if output[1] > 0.5:
                    dino.jump()
            
            dino.motion()
          
            if (not dino.jump_flag and dino.down_flag):
                ge[x].fitness += 0.1

        add_obstacle = False

        rem = []
        
        for obstacle in obstacles:
            for x, dino in enumerate(dinos):
                if obstacle.collide(dino):
                    ge[x].fitness -= 1
                    dinos.pop(x)
                    nets.pop(x)
                    ge.pop(x)
            
                if not obstacle.passed and (obstacle.x + obstacle.img.get_width()) < dino.x:
                    obstacle.passed = True

            if obstacle.x + obstacle.img.get_width() < 0:
                rem.append(obstacle)
            
            if (obstacle.x == dino.x):
                score += 1

            obstacle.move()
            
            if obstacle.passed:
                for g in ge:
                    g.fitness += 5
        
        for r in rem:
            obstacles.remove(r)

        adding_obstacle(obstacles)

        population_size = len(dinos)

        status["score"] = score
        status["generation"] = generation
        status["population_size"] = population_size


        background.move()
        base.move()
        draw_window(win, background, dinos, obstacles, base, status)

def run(config_path: os.path) -> None:
    config_neat = neat.config.Config(neat.DefaultGenome,            
                                neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, 
                                neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config_neat)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    MAX_GEN = int(config('MAXGENERATIONS'))
    winner = p.run(main,MAX_GEN) 