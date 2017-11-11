import game_framework
import title_state
from pico2d import *

import main_state

name = "PauseState"
image = None
logo_time = 0.0
counter = 0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del (image)


def update():
    global counter
    counter = (counter + 1) % 100
    pass


def draw():
    global image
    global counter
    clear_canvas()
    main_state.draw_main_scene()
    if counter < 50:
        image.draw(400, 300)

    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        #다시 p가 눌리면 이전 state로 돌아간다.
        elif (event.type, event.key) == (SDL_KEYDOWN , SDLK_p):
            game_framework.pop_state()

    pass


def pause(): pass


def resume(): pass




