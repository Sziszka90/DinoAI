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

    height_of_obstacle = [obstacles[obstacle_ind].img.get_height()]

    width_of_obstacle = [obstacles[obstacle_ind].img.get_width()]

    height_pos_obstacle = [obstacles[obstacle_ind].y]

    dino_pos = [dino.y]

    obstacle_type = [obstacles[obstacle_ind].type]
  
    return distance_to_obstacle + height_of_obstacle + width_of_obstacle + height_pos_obstacle + dino_pos + obstacle_type