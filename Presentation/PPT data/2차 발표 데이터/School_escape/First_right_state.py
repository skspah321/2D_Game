import game_framework
import title_state
from pico2d import *
import map_01
import Character
import main_state
import All_map

image = None
Background = None
boy = None
enemy = None

def enter():
    global boy, enemy, Background
    All_map.First_Floor_center = False
    All_map.First_Floor_left = False
    All_map.First_Floor_right = True

    if All_map.First_Floor_right:
        Background = map_01.TileMap('Maps\\1F_right.json', map_01.canvasWidth, map_01.canvasHeight)
        boy = Character.Charater((Background.obj_data_list[0][3] + Background.obj_data_list[0][1]) // 2,
                                 (Background.obj_data_list[0][4] + Background.obj_data_list[0][2]) // 2)

        All_map.x = (Background.obj_data_list[0][3] + Background.obj_data_list[0][1]) // 2
        All_map.y = (Background.obj_data_list[0][4] + Background.obj_data_list[0][2]) // 2
        # boy = Character.Charater(400,300)

def exit():
    pass

def update(frame_time):
    handle_events(frame_time)
    Background.update(frame_time)
    boy.update(frame_time)
    #enemy.update(frame_time, boy.pos)


def draw(frame_time):
    # Game Rendering
    clear_canvas()
    Background.draw()
   #enemy.draw()
    boy.draw()
    draw_rectangle(boy.left_a, boy.bottom_a, boy.right_a, boy.top_a)
    #draw_rectangle(enemy.left_a, enemy.bottom_a, enemy.right_a, enemy.top_a)
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            Background.handle_events(event)
            boy.handle_event(event)


def pause(): pass


def resume(): pass




