from nn_config import *
from decouple import config as get_env_var
from utils import replay_genome

check_training = (get_env_var('TRAINING'))

local_dir = os.path.dirname(__file__) 
config_path = os.path.join(local_dir, "config.txt")
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

if(check_training == 'TRUE'):
    run(config) 
elif(check_training == 'FALSE'):
    main_solution(replay_genome("winner.pkl"), config)
else:
    print("Enter a valid state (TRUE or FALSE) for TRAINING!")
