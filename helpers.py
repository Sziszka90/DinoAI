from __future__ import annotations
import os
import sys
import pickle
import json
import neat
from tkinter import messagebox
from tkinter import *


speed = 20
difficulty_name = ''


def get_win_size() -> tuple:
    WIN_HEIGHT = 700
    WIN_WIDTH = 1200
    return (WIN_WIDTH, WIN_HEIGHT)

def get_speed() -> int:
    global speed
    return speed

def get_difficulty_name() -> str:
    global difficulty_name
    return difficulty_name

def set_difficulty(value, difficulty) -> None:
    global speed
    global difficulty_name
    speed = difficulty
    difficulty_name = value[0][0]

def get_max_generations() -> int:
    max_generation = int(get_setup_data()['max_gen'])  

    if(max_generation <= 0 or max_generation > 100):
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Max generations must be between 1 and 100')
        sys.exit()
    else:
        return max_generation

def get_genome_path() -> str:
    data = get_setup_data()    
    genome_name = data['genome_name']
    genome_folder = data['genome_folder']
    genome_path = os.path.join('resources', genome_folder)

    if(genome_folder == ''):
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Please give a genome folder')
        sys.exit()

    if(not os.path.exists(genome_path)):
        os.makedirs(genome_path)

    if(genome_name == ''):
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Please give a genome name')
        sys.exit()
    else:
        return os.path.join(genome_path, (genome_name + '_' + str(difficulty_name)))

def get_genome(genome_path: str) -> neat.DefaultGenome:
    try:
        with open(genome_path, 'rb') as f:
            genome = pickle.load(f)
    except IOError:
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Error while opening genome')
        sys.exit()

    return genome

def check_genome_path() -> bool:
    if os.path.exists(get_genome_path()):
        print('****** Running existing genome... ******')
        return True
    else:
        print('****** Genome does not exist! ******')
        print('****** Running training... ******')
        return False

def get_config_path() -> str:
    data = get_setup_data()  
    config_name = data['config_name']
    config_path = os.path.join('resources', config_name)

    if(config_name == ''):
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Please give a config name')
        sys.exit()
    
    if os.path.exists(config_path):
        return config_path
    else:
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Cannot find config file')
        sys.exit()  

def get_network_graph_path() -> str:
    data = get_setup_data()
    genome_folder = data['genome_folder']
    genome_path = os.path.join('resources', genome_folder)

    if(genome_folder == ''):
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Please give a genome folder')
        sys.exit()

    if(not os.path.exists(genome_path)):
        os.makedirs(genome_path)

    return os.path.join(genome_path, ('NeuralNetwork' + '_' + str(difficulty_name)))
       
def check_network_graph_path() -> str:
    if(os.path.exists(get_network_graph_path())):
        return True
    else:
        Tk().wm_withdraw()
        messagebox.showinfo('Info', 'Network file does not exist')
        return False

def increase_score(velocity: int,score: int) -> int:
    new_score = score + velocity/1000
    return new_score

def get_enviroment(dino: 'Dino', obstacles: list, obstacle_ind: int) -> list:
    distance_to_obstacle = [obstacles[obstacle_ind].x - (dino.x + dino.img.get_width())]
    width_of_obstacle = [obstacles[obstacle_ind].img.get_width()]
    height_of_obstacle = [obstacles[obstacle_ind].img.get_height()]
    distance_from_ground = [(620 - (obstacles[obstacle_ind].y + obstacles[obstacle_ind].img.get_height()))]

    return distance_to_obstacle + width_of_obstacle + height_of_obstacle + distance_from_ground

def get_node_names() -> dict:
    return convert_json_dict_key(get_setup_data()['node_names'])

def convert_json_dict_key(data_with_str: dict) -> dict:
    data_with_int = {}
    for key in data_with_str.keys():
        key_int = int(key)
        data_with_int[key_int] = data_with_str[key]
    
    return data_with_int

def check_images(images: tuple):
    if not os.path.exists('resources'):
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Resources folder does not exist')
        sys.exit()

    if(os.path.exists('resources/images')):
        not_exist = [img for img in images if not os.path.exists(os.path.join('resources/images',img))]
        if (len(not_exist) > 0):
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Image(s) not found')
            sys.exit()
    else:
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Images folder does not exist')
        sys.exit()

def get_images(name: str) -> tuple:
    return tuple(get_setup_data()[name])

def get_setup_data() -> dict:
    if not os.path.exists('resources'):
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Resources folder does not exist')
        sys.exit()

    try:
        with open('resources/setup.json') as f:
            data = json.load(f)
    except IOError:
        Tk().wm_withdraw()
        messagebox.showerror('Error', 'Error while opening setup.json')
        sys.exit()

    return data   