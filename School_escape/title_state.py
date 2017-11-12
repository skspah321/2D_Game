<<<<<<< HEAD
import game_framework
from pico2d import *
import main_state
import random

name = "TitleState"
image = None  #배경
image_2 = None #글씨
image_3 = None #테두리
edge_num = 0
num = 1.0
count = 0.001

New_game_button = False
Continue_game_button = False
Edit_game_button = False
Exit_game_button = False

def enter():
    global image, image_2, image_3
    image = load_image('image\\background.png')
    image_2 = load_image('image\\title_02.png')
    image_3 = load_image('image\\edge_01.png')

def exit():
    global image,image_2
    del(image,image_2)


def handle_events():
    global edge_num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                if edge_num <= 0 and edge_num > -150:
                    edge_num -= 50
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if edge_num >= -150 and edge_num < 0:
                    edge_num += 50
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
                if New_game_button:
                    game_framework.change_state(main_state)
                elif Continue_game_button:
                    pass
                elif Edit_game_button:
                    pass
                elif Exit_game_button:
                    game_framework.quit()




def draw():
    global num,edge_num
    clear_canvas()
    image.draw(400,300,870,680)
    image_2.draw(650,200,220,170)
    image_3.draw(648,276+edge_num,255,35)
    image.opacify(num)

    update_canvas()



def update():
    global num, count, edge_num
    global New_game_button, Continue_game_button, Edit_game_button, Exit_game_button
    num -= count
    if num < 0.75 or num > 1.0 :
        count = -count
    if edge_num == 0:
        New_game_button = True
        Continue_game_button = False
        Edit_game_button = False
        Exit_game_button = False
    if edge_num == -50:
        Continue_game_button = True
        New_game_button = False
        Edit_game_button = False
        Exit_game_button = False
    if edge_num == -100:
        Edit_game_button = True
        New_game_button = False
        Continue_game_button = False
    if edge_num == -150:
        Exit_game_button= True
        New_game_button = False
        Continue_game_button = False
        Edit_game_button = False




def pause():
    pass


def resume():
    pass






=======
import game_framework
from pico2d import *
import main_state
import pygame

import random
pygame.mixer.init()

name = "TitleState"
image = None   #배경
image_2 = None #글씨
image_3 = None  #테두리
edge_num = 0
num = 1.0
count = 0.001

title_move = None
title_click = None
title_main = None
title_exit = None

New_game_button = False
Continue_game_button = False
Edit_game_button = False
Exit_game_button = False

def enter():
    global image, image_2, image_3
    global title_main, title_click, title_exit, title_move
    image = load_image('image\\background.png')
    image_2 = load_image('image\\title_02.png')
    image_3 = load_image('image\\edge_01.png')

    title_move = pygame.mixer.Sound("sound\\title_move.wav")
    title_click = pygame.mixer.Sound("sound\\title_click.wav")
    title_main = pygame.mixer.Sound("sound\\title_main.wav")
    title_exit = pygame.mixer.Sound("sound\\title_exit.wav")

    title_main.play()

def exit():
    global image,image_2, image_3
    global title_main, title_click, title_exit, title_move

    title_main.stop()
    title_exit.stop()
    title_move.stop()
    title_click.stop()

    del(image, image_2, image_3)
    del(title_main, title_click, title_exit, title_move)


def handle_events():
    global edge_num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                if edge_num <= 0 and edge_num > -150:
                    title_move.play()
                    edge_num -= 50
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                if edge_num >= -150 and edge_num < 0:
                    title_move.play()
                    edge_num += 50
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
                if New_game_button:
                    title_click.play()
                    delay(1.0)
                    game_framework.change_state(main_state)
                elif Continue_game_button:
                    title_click.play()
                    delay(1.0)
                    pass
                elif Edit_game_button:
                    title_click.play()
                    delay(0.5)
                    pass
                elif Exit_game_button:
                    title_exit.play()
                    delay(0.5)
                    game_framework.quit()




def draw():
    global num,edge_num
    clear_canvas()
    image.draw(400,300,870,680)
    image_2.draw(650,200,220,170)
    image_3.draw(648,276+edge_num,255,35)
    image.opacify(num)

    update_canvas()



def update():
    global num, count, edge_num
    global New_game_button, Continue_game_button, Edit_game_button, Exit_game_button
    num -= count
    if num < 0.75 or num > 1.0 :
        count = -count
    if edge_num == 0:
        New_game_button = True
        Continue_game_button = False
        Edit_game_button = False
        Exit_game_button = False
    if edge_num == -50:
        Continue_game_button = True
        New_game_button = False
        Edit_game_button = False
        Exit_game_button = False
    if edge_num == -100:
        Edit_game_button = True
        New_game_button = False
        Continue_game_button = False
    if edge_num == -150:
        Exit_game_button= True
        New_game_button = False
        Continue_game_button = False
        Edit_game_button = False




def pause():
    pass


def resume():
    pass






>>>>>>> 33b076c4419c5f97ff9469ab78ec4ed4855d19ec
