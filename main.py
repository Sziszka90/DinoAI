from nn_config import *
from decouple import config as get_env_var
from utils import *
from plot import plot

local_dir = os.path.dirname(__file__) 
config_path = os.path.join(local_dir, check_config_path())
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

genome_path = check_genome_path()

if(genome_path):
    main_solution(replay_genome(genome_path), config)
else:
    run(config)
    plot()