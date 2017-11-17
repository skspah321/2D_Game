import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state

name = "MainState"
import Character

boy = None
glass = None
Running = True

#current_time = 0.0

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


def enter():
    global boy,glass
    glass = Grass()
    boy = Character.Charater()


def exit():
    global boy,glass
    del(boy)
    del(glass)


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global Running#, current_time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)

def update(frame_time):
    #global current_time
    #frame_time = get_frame_time()
    handle_events(frame_time)
    boy.update(frame_time)
    #print(frame_time)


def draw_main_scene():
    boy.draw()


def draw(frame_time):
   # Game Rendering
   clear_canvas()
   glass.draw()
   boy.draw()
   update_canvas()


def get_frame_time():
    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time
