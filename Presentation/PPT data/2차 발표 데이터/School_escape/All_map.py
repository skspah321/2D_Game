import Character
import map_01
import main_state


First_Floor_center = False
First_Floor_right = False
First_Floor_left = False

First_Floor_left_class = False
First_Floor_right_class = False

First_Floor_left_science = False
First_Floor_left_nursing = False

Second_Floor_center = False
Second_Floor_office = False
Second_Floor_library = False


x = 0
y = 0


#현재 캐릭터 좌표
character_x = 0
character_y = 0

character_direction = (character_x,character_y)
#현재 캐릭터가 있는 타일
character_x_tile = 0
character_y_tile = 0

speed = 0

all_obj_data = []