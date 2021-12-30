from nn_config import *
from decouple import config as get_env_var
from utils import *
from plot import plot

local_dir = os.path.dirname(__file__) 
config_path = os.path.join(local_dir, "config.txt")
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

if (check_model("winner.pkl")):
    main_solution(replay_genome("winner.pkl"), config)
else:
    run(config)
    plot()