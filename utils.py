import sys
from dino import *

def check_speed(VEL: int) -> None:
    if(VEL < 10):
        print("Increase speed! Min. 10")
        sys.exit()
    elif(VEL > 20):
        print("Reduce speed! Max. 20")
        sys.exit()

def direction(dino: Dino, obstacles: list, obstacle_ind: int) -> list:

    distance_to_obstacle = [obstacles[obstacle_ind].x - (dino.x + dino.img.get_width())]

    width_of_obstacle = [obstacles[obstacle_ind].img.get_width()]

    height_of_obstacle = [obstacles[obstacle_ind].img.get_height()]

    height_obstacle = [obstacles[obstacle_ind].y]

    return distance_to_obstacle + width_of_obstacle + height_obstacle + height_of_obstacle