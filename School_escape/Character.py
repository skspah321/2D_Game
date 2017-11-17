from pico2d import *
import random

class Charater:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀 , 30CM
    RUN_SPEED_KMPH = 10.0  # KM / HOUR , 캐릭터가 이동하는 속도
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # 시간당 meter
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # 초당 meter
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # 초당 픽셀, 이걸 프레임타임에 곱해준다.

    image = None
    font = None
    UP_RUN, RIGHT_RUN, LEFT_RUN, DOWN_RUN = 0, 1, 2, 3

    UP_STAND, RIGHT_STAND, LEFT_STAND, DOWN_STAND = 4, 5, 6,7

    def __init__(self):
        self.x, self.y = 400, 300
        self.frame = 0
        self.width_dir = 1  # 가로 방향 벡터
        self.height_dir = 1  # 세로 방향 벡터
        self.state = self.DOWN_STAND
        if Charater.image == None:
            Charater.image = load_image('image\\main_character.png')



    def update(self, frame_time):
        distance = Charater.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 4
        if self.state == self.UP_RUN:
            self.y = self.y + (self.height_dir * distance)
        elif self.state == self.RIGHT_RUN:
            self.x = self.x +(self.width_dir * distance)
        elif self.state == self.LEFT_RUN:
            self.x = self.x + (self.width_dir * distance)
        elif self.state == self.DOWN_RUN:
            self.y = self.y + (self.height_dir * distance)
        elif self.state == self.UP_STAND:
            self.y = self.y + 0.0
        elif self.state == self.RIGHT_STAND:
            self.x = self.x + 0.0
        elif self.state == self.LEFT_STAND:
            self.x = self.x + 0.0
        elif self.state == self.DOWN_STAND:
            self.y = self.y + 0.0

    def handle_event(self, event):
        if (event.type,event.key) == (SDL_KEYDOWN ,SDLK_UP):
            if self.state in (self.RIGHT_STAND,self.DOWN_STAND,self.LEFT_STAND,self.UP_STAND,self.DOWN_RUN,
                              self.LEFT_RUN,self.RIGHT_RUN):
                self.state = self.UP_RUN
                self.height_dir = 1
        elif (event.type,event.key) == (SDL_KEYDOWN ,SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.DOWN_STAND, self.LEFT_STAND, self.UP_STAND, self.DOWN_RUN,
                              self.LEFT_RUN,self.UP_RUN):
                self.state = self.RIGHT_RUN
                self.width_dir = 1
        elif (event.type,event.key) == (SDL_KEYDOWN ,SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.DOWN_STAND, self.LEFT_STAND, self.UP_STAND, self.DOWN_RUN,
                              self.RIGHT_RUN,self.UP_RUN):
                self.state = self.LEFT_RUN
                self.width_dir = -1
        elif (event.type,event.key) == (SDL_KEYDOWN ,SDLK_DOWN):
            if self.state in (self.RIGHT_STAND, self.DOWN_STAND, self.LEFT_STAND, self.UP_STAND, self.RIGHT_RUN,
                              self.LEFT_RUN,self.UP_RUN):
                self.state = self.DOWN_RUN
                self.height_dir = -1
        elif (event.type,event.key) == (SDL_KEYUP ,SDLK_UP):
                if self.state in (self.UP_RUN,):
                    self.state = self.UP_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
                if self.state in (self.RIGHT_RUN,):
                    self.state = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                if self.state in (self.LEFT_RUN,):
                    self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
                if self.state in (self.DOWN_RUN,):
                    self.state = self.DOWN_STAND

    def draw(self):
        if self.state in [self.UP_RUN, self.DOWN_RUN, self.LEFT_RUN, self.RIGHT_RUN]:
            self.image.clip_draw(self.frame * 50, self.state*85, 50, 85, self.x, self.y,50,50)
        else:
            self.image.clip_draw((self.frame * 50) % 50, self.state % 4 * 85, 50, 85, self.x, self.y,50,50)






