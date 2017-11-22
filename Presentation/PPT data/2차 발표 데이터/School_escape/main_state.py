import random
import json
import os

from pico2d import *
import game_framework
import title_state
import map_01
import Character
import Enemy
import All_map
import First_left_state
import Camera


name = "MainState"

boy = None
enemy = None
Running = True
Background = None
Cam = None

check_flag = 0

def collision(a,aa,bb,cc,dd):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = (aa,bb,cc,dd)

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a > bottom_b: return False
    if bottom_a < top_b: return False

    print("충돌!!!")

    return True

def enter():
    global boy, enemy, Background,Cam
    All_map.First_Floor_center = True

    if All_map.First_Floor_center:
        Background = map_01.TileMap('Maps\\1F_center.json', map_01.canvasWidth, map_01.canvasHeight)
        enemy = Enemy.Enemy(0, 0)
        boy = Character.Charater((Background.obj_data_list[0][3] + Background.obj_data_list[0][1]) // 2,
                                 (Background.obj_data_list[0][4] + Background.obj_data_list[0][2]) // 2)
        All_map.x = (Background.obj_data_list[0][3] + Background.obj_data_list[0][1]) // 2
        All_map.y = (Background.obj_data_list[0][4] + Background.obj_data_list[0][2]) // 2

    #현재 캐릭터 좌표, 타일위치를 저장
    All_map.character_x = boy.x
    All_map.character_y = boy.y
    All_map.character_x_tile = boy.x // 32
    All_map.character_y_tile = boy.y // 32

    #Cam = Camera.Camera(800,600)

def exit():
   pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global Running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type,event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            Background.handle_events(event)
            boy.handle_event(event)


def update(frame_time):
    handle_events(frame_time)
    Background.update(frame_time)
    boy.update(frame_time)
    enemy.update(frame_time,boy.pos)
    for i in Background.obj_data_list:
        if i[0] == "character_left":
            if collision(boy, i[1],i[2],i[3],i[4]):
                game_framework.change_state(First_left_state)

        if i[0] == "wall":
            if collision(boy, i[1], i[2], i[3], i[4]):
                boy.stop()
       # if i[0] == "character_right":
           # if collision(boy, i[1],i[2],i[3],i[4]):
               #game_framework.push_state(First_right_state)

    All_map.character_x = boy.x
    All_map.character_y = boy.y
    All_map.character_x_tile = boy.x // 32
    All_map.character_y_tile = boy.y // 32
    #print(boy.x, boy.y)



    #print(All_map.character_x,All_map.character_y,All_map.character_x_tile,All_map.character_y_tile)



    #print("캐릭터좌표: ", boy.x, boy.y)

    #Cam.update(boy)





def draw(frame_time):
   # Game Rendering
   global check_flag
   clear_canvas()
   Background.draw()
   #enemy.draw()
   boy.draw()
   draw_rectangle(boy.left_a,boy.bottom_a,boy.right_a, boy.top_a)
   #draw_rectangle(enemy.left_a,enemy.bottom_a,enemy.right_a, enemy.top_a)
   update_canvas()


