import game_framework
import title_state
from pico2d import *
import map_01
import Character
import main_state
import All_map
import First_left_state
import First_right_state


image = None
Background = None
boy = None
enemy = None
count = 0

def collision(a,aa,bb,cc,dd):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = (aa,bb,cc,dd)

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a > bottom_b: return False
    if bottom_a < top_b: return False

    return True


def enter():
    global boy, Background,count
    Background = map_01.TileMap('Maps\\1F_center.json', map_01.canvasWidth, map_01.canvasHeight)

    for i in Background.obj_data_list:
        count +=1
        print(i)
        if i[0] == "left_start":
            print(count)



    if All_map.First_Floor_left:  # 이전 방이 왼쪽이였다면
        boy = Character.Charater((Background.obj_data_list[14][3] + Background.obj_data_list[14][1]) // 2,
                                 (Background.obj_data_list[14][4] + Background.obj_data_list[14][2]) // 2)

        All_map.x = (Background.obj_data_list[14][3] + Background.obj_data_list[14][1]) // 2
        All_map.y = (Background.obj_data_list[14][4] + Background.obj_data_list[14][2]) // 2

    All_map.First_Floor_center = False
    All_map.First_Floor_left = False
    All_map.First_Floor_center = True

    # 현재 캐릭터 좌표, 타일위치를 저장
    All_map.character_x = boy.x
    All_map.character_y = boy.y
    All_map.character_x_tile = boy.x // 32
    All_map.character_y_tile = boy.y // 32


def exit():
    pass

def update(frame_time):
    handle_events(frame_time)
    Background.update(frame_time)
    boy.update(frame_time)
    for i in Background.obj_data_list:
        if i[0] == "character_left":
            if collision(boy, i[1],i[2],i[3],i[4]):
                game_framework.change_state(First_left_state)
    #enemy.update(frame_time, boy.pos)

    All_map.character_x = boy.x
    All_map.character_y = boy.y
    All_map.character_x_tile = boy.x // 32
    All_map.character_y_tile = boy.y // 32


def draw(frame_time):
    # Game Rendering
    clear_canvas()
    Background.draw()
    boy.draw()
    draw_rectangle(boy.left_a, boy.bottom_a, boy.right_a, boy.top_a)
    # draw_rectangle(enemy.left_a, enemy.bottom_a, enemy.right_a, enemy.top_a)
    update_canvas()
    #enemy.draw()


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




