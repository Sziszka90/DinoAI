import subprocess
import neat
from agents import run, winner_play, manual_play
from plot import plot
from visualize_network import draw_net
import helpers


def ai_selected() -> None:
    config_path = helpers.get_config_path()
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    if(helpers.check_genome_path()):
        winner_play(helpers.get_genome(helpers.get_genome_path()), config)
    else:
        run(config)
        draw_net(config, helpers.get_genome(helpers.get_genome_path()), filename=helpers.get_network_graph_path(), node_names=helpers.get_node_names())
        plot()

def manual_selected() -> None:
    manual_play()

def retrain_selected() -> None:
    config_path = helpers.get_config_path()
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    run(config) 
    draw_net(config, helpers.get_genome(helpers.get_genome_path()), filename=helpers.get_network_graph_path(), node_names=helpers.get_node_names())
    plot()   

def open_network_selected() -> None:
    if helpers.check_network_graph_path():
        path = helpers.get_network_graph_path() + '.pdf'
        proc = subprocess.Popen([path], shell=True)

        try:
            proc.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()
    else:
        pass
