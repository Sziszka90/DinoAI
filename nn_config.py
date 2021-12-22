import neat
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from cactus import *
from base import *
from dino import *
from draw import *
from utils import directions
import pickle

WIN_WIDTH = 1200
WIN_HEIGHT = 700

generation = 0

def main_training(genomes: neat.DefaultGenome, config: neat.Config) -> None:
    print("****** Running training... ******")
    nets = []
    ge = []
    dinos = []
    base = Base()
    obstacles = [Bird(495)]
    background = Background()
    reset_adding_obstacle()
    score = 0
    global generation
    generation += 1
    population_size = 0
    status = {}
    max_fitness = 0
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    for _, g in genomes: 
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)  
        dinos.append(Dino())
        g.fitness = 0 
        ge.append(g)

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
            output = nets[x].activate(directions(dino, obstacles, obstacle_ind))

            if output[0] > output[1] and output[0] > 0.5:
                dino.jump()
            elif output[1] > output[0] and output[1] > 0.5:
                dino.down()

            dino.motion()
          
            ge[x].fitness += 0.1

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

            score += 0.01
            
            obstacle.move()
            
            if obstacle.passed:
                for g in ge:
                    g.fitness += 5
                    if(g.fitness > max_fitness):
                        max_fitness = g.fitness
        
        for r in rem:
            obstacles.remove(r)

        adding_obstacle(obstacles)

        population_size = len(dinos)

        if(max_fitness > config.fitness_threshold):
            print("****** Solution found! ******")
            run = False

        status["Score: "] = round(score)
        status["Fitness score: "] = round(max_fitness)
        status["Generation: "] = generation
        status["Population size: "] = population_size
        
        background.move()
        base.move()
        draw_window(win, background, dinos, obstacles, base, status)

def main_solution(genome: neat.DefaultGenome, config: neat.Config) -> None:
    print("****** Running solution... ******")
    base = Base()
    obstacles = [Bird(495)]
    background = Background()
    dino = Dino()
    score = 0
    status = {}
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
     
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    run = True

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                
        obstacle_ind = 0
        
    
        if ((len(obstacles) > 1) and (dino.x > obstacles[0].x + obstacles[0].img.get_width())):
            obstacle_ind = 1
    
        
        output = net.activate(directions(dino, obstacles, obstacle_ind))

        if output[0] > output[1] and output[0] > 0.5:
            dino.jump()
        elif output[1] > output[0] and output[1] > 0.5:
            dino.down()

        dino.motion()

        rem = []
        
        for obstacle in obstacles:
            if obstacle.collide(dino):
                run = False
            
            if not obstacle.passed and (obstacle.x + obstacle.img.get_width()) < dino.x:
                obstacle.passed = True

            if obstacle.x + obstacle.img.get_width() < 0:
                rem.append(obstacle)

            score += 0.01
            
            obstacle.move()
        
        for r in rem:
            obstacles.remove(r)

        adding_obstacle(obstacles)

        status["Score: "] = round(score)
        status["Generation: "] = "Winner"
        status["Population size: "] = 1

        background.move()
        base.move()
        draw_window(win, background, [dino], obstacles, base, status)

def run(config: neat.Config) -> None:
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    MAXGENERATIONS = int(get_env_var('MAXGENERATIONS'))

    winner = p.run(main_training, MAXGENERATIONS)

    pickle.dump( winner, open( "winner.pkl", "wb"))