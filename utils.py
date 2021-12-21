import sys
from dino import *

def check_speed(VEL: int) -> None:
    if(VEL < 20):
        print("Increase speed! Min. 20")
        sys.exit()
    elif(VEL > 30):
        print("Reduce speed! Max. 30")
        sys.exit()

def directions(dino: Dino, obstacles: list, obstacle_ind: int) -> list:

    distance_to_obstacle = [obstacles[obstacle_ind].x - (dino.x + dino.img.get_width())]

    width_of_obstacle = [obstacles[obstacle_ind].img.get_width()]

    height_of_obstacle = [obstacles[obstacle_ind].img.get_height()]

    distance_from_ground = [(620 - (obstacles[obstacle_ind].y + obstacles[obstacle_ind].img.get_height()))]

    return distance_to_obstacle + width_of_obstacle + height_of_obstacle + distance_from_ground
