import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import sys
import pickle
import pygame
import neat
from obstacles import Bird
from track import Track
from background import Background
from dino import Dino
from draw import Draw
from plot import collect_data
import helpers


generation = 0
start = False


def training_play(genomes: neat.DefaultGenome, config: neat.Config) -> None:
    global generation
    global start

    nets = []
    ge = []
    dinos = []
    velocity = helpers.get_speed()

    obstacles = [Bird('up', velocity)]
    track = Track(velocity)
    background = Background(velocity)
    draw = Draw(velocity)
    
    score = 0
    population_size = 0
    status = {}
    max_fitness = 0

    win = pygame.display.set_mode(helpers.get_win_size())
    clock = pygame.time.Clock()

    generation += 1

    draw.reset_adding_obstacle()
    
    for _, g in genomes: 
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)  
        dinos.append(Dino())
        g.fitness = 0 
        ge.append(g)

    run = True
    
    while run:
        draw.draw_window(win, background, dinos, obstacles, track, status, start)

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        if(start):
            obstacle_ind = 0
            
            if len(dinos) > 0:
                if ((len(obstacles) > 1) and (dinos[0].x > obstacles[0].x + obstacles[0].img.get_width())):
                    obstacle_ind = 1
            else:
                run = False
                break
            
            for x, dino in enumerate(dinos):
                output = nets[x].activate(helpers.get_enviroment(dino, obstacles, obstacle_ind))

                if output[0] > output[1] and output[0] > 0.5:
                    dino.jump = True
                elif output[1] > output[0] and output[1] > 0.5:
                    dino.down = True

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

                score = helpers.increase_score(velocity,score)
                
                if obstacle.passed:
                    for g in ge:
                        g.fitness += 5
                        if(g.fitness > max_fitness):
                            max_fitness = g.fitness

                obstacle.move()
            
            for r in rem:
                obstacles.remove(r)

            population_size = len(dinos)

            if(max_fitness > config.fitness_threshold):
                print('****** Solution found! ******')
                run = False

            status['Score: '] = round(score)
            status['Fitness score: '] = round(max_fitness)
            status['Generation: '] = generation
            status['Population size: '] = population_size
            status['Difficulty: '] = helpers.get_difficulty_name()
        
            draw.adding_obstacle(obstacles)

            background.move()
            track.move()

            if(len(dinos) == 0 or not run):
                collect_data(status['Fitness score: '], status['Generation: '])

        else:  
            if pygame.key.get_pressed()[pygame.K_SPACE] and not start:
                start = True

            for dino in dinos:
                dino.motion()
            background.move()
            track.move()

def winner_play(genome: neat.DefaultGenome, config: neat.Config) -> None:
    global start

    net = neat.nn.FeedForwardNetwork.create(genome, config)
    velocity = helpers.get_speed()

    track = Track(velocity)
    obstacles = [Bird('up',velocity)]
    background = Background(velocity)
    dino = Dino()
    draw = Draw(velocity)

    score = 0
    status = {}

    win = pygame.display.set_mode(helpers.get_win_size())
    clock = pygame.time.Clock()
     
    gameover = False
    run = True
    
    while run:
        draw.draw_window(win, background, [dino], obstacles, track, status, start, gameover)

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        if pygame.key.get_pressed()[pygame.K_q]:
            start = False
            run = False

        if(start):       
            obstacle_ind = 0
            
            if ((len(obstacles) > 1) and (dino.x > obstacles[0].x + obstacles[0].img.get_width())):
                obstacle_ind = 1
            
            output = net.activate(helpers.get_enviroment(dino, obstacles, obstacle_ind))

            if output[0] > output[1] and output[0] > 0.5:
                dino.jump = True
            elif output[1] > output[0] and output[1] > 0.5:
                dino.down = True

            dino.motion()

            rem = []
            
            for obstacle in obstacles:
                if obstacle.collide(dino):
                    gameover = True
                    start = False
                
                if not obstacle.passed and (obstacle.x + obstacle.img.get_width()) < dino.x:
                    obstacle.passed = True

                if obstacle.x + obstacle.img.get_width() < 0:
                    rem.append(obstacle)

                score = helpers.increase_score(velocity,score)
                
                obstacle.move()
            
            for r in rem:
                obstacles.remove(r)

            status['Score: '] = round(score)
            status['Player: '] = 'AI'
            status['Population size: '] = 1
            status['Difficulty: '] = helpers.get_difficulty_name()

            draw.adding_obstacle(obstacles)

            background.move()
            track.move()

        else:
            draw.reset_adding_obstacle()

            obstacles.clear()
            obstacles = [Bird(480,velocity)]
            score = 0

            if gameover:   
                dino.dead = True
            else:
                track.move()
                
            dino.motion()
            background.move()

            if pygame.key.get_pressed()[pygame.K_SPACE] and not start:
                gameover = False
                start = True

def manual_play() -> None:
    global start

    velocity = helpers.get_speed()

    track = Track(velocity)
    obstacles = [Bird('up',velocity)]
    background = Background(velocity)
    dino = Dino()
    draw = Draw(velocity)

    score = 0
    status = {}

    win = pygame.display.set_mode(helpers.get_win_size())
    clock = pygame.time.Clock()

    run = True
    gameover = False

    while run:
        draw.draw_window(win, background, [dino], obstacles, track, status, start, gameover)

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        if pygame.key.get_pressed()[pygame.K_q]:
            start = False
            run = False

        if(start):       
            if pygame.key.get_pressed()[pygame.K_UP] == True:
                dino.jump = True
            if pygame.key.get_pressed()[pygame.K_DOWN] == True:
                dino.down = True

            dino.motion()

            rem = []
            
            for obstacle in obstacles:
                if obstacle.collide(dino):
                    gameover = True
                    start = False
                
                if not obstacle.passed and (obstacle.x + obstacle.img.get_width()) < dino.x:
                    obstacle.passed = True

                if obstacle.x + obstacle.img.get_width() < 0:
                    rem.append(obstacle)

                score = helpers.increase_score(velocity,score)
                
                obstacle.move()
            
            for r in rem:
                obstacles.remove(r)

            status['Score: '] = round(score)
            status['Player: '] = 'Human'
            status['Population size: '] = 1
            status['Difficulty: '] = helpers.get_difficulty_name()

            draw.adding_obstacle(obstacles)

            background.move()
            track.move()

        else:
            draw.reset_adding_obstacle()
            
            obstacles.clear()
            obstacles = [Bird(480,velocity)]
            score = 0

            if gameover:   
                dino.dead = True
            else:
                track.move()
                
            dino.motion()
            background.move()

            if pygame.key.get_pressed()[pygame.K_SPACE] and not start:
                gameover = False
                start = True

def run(config: neat.Config) -> None:
    global generation
    global start

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(training_play, helpers.get_max_generations())

    generation = 0
    start = False

    pickle.dump( winner, open(helpers.get_genome_path(), 'wb'))