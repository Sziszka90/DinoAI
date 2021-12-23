import sys
from dino import *
import pickle
import neat

def check_speed(VEL: int) -> None:
    if(VEL < 20):
        print("Increase speed! Min. 20")
        sys.exit()
    elif(VEL > 30):
        print("Reduce speed! Max. 30")
        sys.exit()

def check_train(TRAIN: str) -> None:
    if(TRAIN != "YES" and TRAIN != "NO"):
        print("Please enter a valid value for TRAIN (YES or NO)")
        sys.exit()

def check_max_generations(MAXGENERATIONS: int) -> None:
    if(MAXGENERATIONS <= 0 or MAXGENERATIONS > 100):
        print("Max generations must be between 1 and 100")
        sys.exit()

def directions(dino: Dino, obstacles: list, obstacle_ind: int) -> list:

    distance_to_obstacle = [obstacles[obstacle_ind].x - (dino.x + dino.img.get_width())]

    width_of_obstacle = [obstacles[obstacle_ind].img.get_width()]

    height_of_obstacle = [obstacles[obstacle_ind].img.get_height()]

    distance_from_ground = [(620 - (obstacles[obstacle_ind].y + obstacles[obstacle_ind].img.get_height()))]

    return distance_to_obstacle + width_of_obstacle + height_of_obstacle + distance_from_ground

def replay_genome(genome_path: str="winner.pkl") -> neat.DefaultGenome:
    try:
        with open(genome_path, "rb") as f:
            genome = pickle.load(f)
    except IOError:
        print("****** Please train the model! ******")
        sys.exit()

    return genome