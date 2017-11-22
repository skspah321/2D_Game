from pico2d import *
import Character


class Camera:
    def __init__(self,width,height): # width, hegith는 맵 너비랑 높이
        self.camera = draw_rectangle(0,0,width,height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):  # target은 캐릭터
        x = -target.x + int(50 / 2)  # width는 캐릭터 너비
        y = -target.y + int(50 / 2) # height는 캐릭터 높이
        self.camera = draw_rectangle(x, y, self.width, self.height)
