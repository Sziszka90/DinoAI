import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
import pygame_menu
from menu_selection import ai_selected, manual_selected, retrain_selected, open_network_selected
import helpers


pygame.init()

win_size = helpers.get_win_size()
win = pygame.display.set_mode(win_size)
pygame.display.set_caption('Dino AI')

menu = pygame_menu.Menu('Welcome', win_size[0], win_size[1], theme=pygame_menu.themes.THEME_DARK)
menu.add.selector('Difficulty: ', [('Hard', 30), ('Medium', 25), ('Easy', 20)], onchange=helpers.set_difficulty, default=1)
menu.add.button('Manual mode', manual_selected)
menu.add.button('AI mode', ai_selected)
menu.add.button('AI train', retrain_selected)
menu.add.button('Open network', open_network_selected)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(win)

