from nn_config import *
from decouple import config as get_env_var
from utils import *
from plot import plot

check_training = (get_env_var('TRAIN'))

local_dir = os.path.dirname(__file__) 
config_path = os.path.join(local_dir, "config.txt")
config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

check_train(check_training)

if(check_training == 'YES'):
    run(config)
    plot()
elif(check_training == 'NO'):
    main_solution(replay_genome("winner.pkl"), config)
