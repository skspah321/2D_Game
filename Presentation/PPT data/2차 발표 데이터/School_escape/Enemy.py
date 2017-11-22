from pico2d import *
import Character
import math
import random

class Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀 , 30CM
    RUN_SPEED_KMPH = 15.0  # KM / HOUR , 적이 이동하는 속도
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)  # 시간당 meter
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)  # 초당 meter
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # 초당 픽셀, 이걸 프레임타임에 곱해준다.

    image = None

    UP_RUN, RIGHT_RUN, LEFT_RUN, DOWN_RUN = 3, 0, 2, 1

    #UP_STAND, RIGHT_STAND, LEFT_STAND, DOWN_STAND = 7, 4, 6, 5

    def __init__(self, startx, starty):
        self.x, self.y = startx, starty
        self.pos = (self.x,self.y)
        self.frame = 0
        self.width = 64
        self.height = 64
        self.width_dir = 1  # 가로 방향 벡터
        self.height_dir = 1  # 세로 방향 벡터
        self.state = None

        self.left_a = self.x - 17
        self.bottom_a = self.y - 30
        self.right_a = self.x + 15
        self.top_a = self.y + 18

        if Enemy.image == None:
            Enemy.image = load_image('image\\enemy_character.png')

    def update(self, frame_time, Character_pos):
        distance = Enemy.RUN_SPEED_PPS * frame_time  # 적 이동 속도
        self.frame = (self.frame + 1) % 9

        if Character_pos[0] - self.x > 0:  # 캐릭터가 우측에 있다
            self.height_dir = 0
            self.state = self.RIGHT_RUN
            self.width_dir = 1
            self.state_check(distance)
            if Character_pos[1] - self.y > 10:  # 캐릭터가 위에 있다
                self.state = self.UP_RUN
                self.height_dir = 1
                self.state_check(distance)
            elif Character_pos[1] - self.y < -10:  # 캐릭터가 아래에 있다
                self.state = self.DOWN_RUN
                self.height_dir = -1
                self.state_check(distance)

        if Character_pos[0] - self.x < 0:  # 캐릭터가 좌측에 있다
            self.height_dir = 0
            self.state = self.LEFT_RUN
            self.width_dir = -1
            self.state_check(distance)
            if Character_pos[1] - self.y > 10:  # 캐릭터가 위에 있다
                self.state = self.UP_RUN
                self.height_dir = 1
                self.state_check(distance)
            elif Character_pos[1] - self.y < -10:  # 캐릭터가 아래에 있다
                self.state = self.DOWN_RUN
                self.height_dir = -1
                self.state_check(distance)

    def state_check(self,distance):
        if self.state == self.UP_RUN:
            self.y = self.y + (self.height_dir * distance)
        if self.state == self.RIGHT_RUN:
            self.x = self.x + (self.width_dir * distance)
        if self.state == self.LEFT_RUN:
            self.x = self.x + (self.width_dir * distance)
        if self.state == self.DOWN_RUN:
            self.y = self.y + (self.height_dir * distance)



        self.left_a = self.x - 17
        self.bottom_a = self.y - 30
        self.right_a = self.x + 15
        self.top_a = self.y + 18

        self.pos = (self.x, self.y)

    def draw(self):
        if self.state in [self.UP_RUN, self.DOWN_RUN, self.LEFT_RUN, self.RIGHT_RUN]:
            self.image.clip_draw(self.frame * 64, self.state*64, 64, 64, self.x, self.y,60,60)







