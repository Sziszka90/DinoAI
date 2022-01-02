from training_solution import *
from helpers import *
from plot import plot

local_dir = os.path.dirname(__file__) 
config_path = os.path.join(local_dir, check_config_path())
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

if(check_genome_path()):
    solution(replay_genome(return_genome_path()), config)
else:
    run(config)
    plot()