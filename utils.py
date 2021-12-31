import sys
from dino import *
import pickle
import neat
from decouple import config as get_env_var

def handle_speed(velocity: int) -> int:
    if(velocity <= 0):
        print("Increase speed! Min. 1")
        sys.exit()
    elif(velocity > 10):
        print("Reduce speed! Max. 10")
        sys.exit()
    else:
        return velocity+20

def check_max_generations() -> int:
    maxgenerations = int(get_env_var('MAXGENERATIONS'))
    if(maxgenerations <= 0 or maxgenerations > 100):
        print("Max generations must be between 1 and 100")
        sys.exit()
    else:
        return maxgenerations

def check_genome_path() -> str:
    genome_path = get_env_var('GENOME_NAME')
    if(genome_path != ""):
        if(os.path.exists('./' + genome_path)):
            return genome_path
        else:
            print("****** Start genome training! ******")
            return None
    else:
        print("Please give a genome path")
        sys.exit()
    
def return_genome_path() -> str:
    return get_env_var('GENOME_NAME')

def check_config_path() -> str:
    config_path = get_env_var('CONFIG_NAME')
    if(config_path != ""):
        if(os.path.exists('./' + config_path)):
            return config_path
        else:
            print("Config not found")
            sys.exit()
    else:
        print("Please give a config path")
        sys.exit()

def increase_score(velocity: int,score: int) -> int:
    new_score = score + velocity/1000
    return new_score

def directions(dino: Dino, obstacles: list, obstacle_ind: int) -> list:

    distance_to_obstacle = [obstacles[obstacle_ind].x - (dino.x + dino.img.get_width())]

    width_of_obstacle = [obstacles[obstacle_ind].img.get_width()]

    height_of_obstacle = [obstacles[obstacle_ind].img.get_height()]

    distance_from_ground = [(620 - (obstacles[obstacle_ind].y + obstacles[obstacle_ind].img.get_height()))]

    return distance_to_obstacle + width_of_obstacle + height_of_obstacle + distance_from_ground

def replay_genome(genome_path: str) -> neat.DefaultGenome:
    try:
        with open(genome_path, "rb") as f:
            genome = pickle.load(f)
    except IOError:
        sys.exit()

    return genome
