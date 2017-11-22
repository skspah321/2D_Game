from pico2d import*
import Character
import All_map
import game_framework

canvasWidth = 800
canvasHeight = 600

check_flag = False

class TileMap:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀 , 30CM
    SCROLL_KMPH = 20.0  # KM / HOUR , 캐릭터가 이동하는 속도랑 맞춰줌
    SCROLL_MPM = (SCROLL_KMPH * 1000.0 / 60.0)  # 시간당 meter
    SCROLL_MPS = (SCROLL_MPM / 60.0)  # 초당 meter
    SCROLL_PPS = (SCROLL_MPS * PIXEL_PER_METER)  # 초당 픽셀, 이걸 프레임타임에 곱해준다.

    def __init__(self,filename, width, height):
        f = open(filename)
        self.map = json.load(f)  # 제이슨 파일 오픈

        #self.x = All_map.character_x_tile
        #self.y = All_map.character_y_tile


        self.map_w = self.map["width"]  # 맵 너비
        self.map_h = self.map["height"]  # 맵 높이
        self.x = 0
        self.y = 0
        self.layerindex = {"Layer_01": 0, "Layer_02": 1, "Layer_03": 2, "Object_01": 3}  # 몇번째 레이어 인지
        self.obj_list = []   # 오브젝트를 리스트로 정리
        self.obj_data_list = [] # 오브젝트 x,y.. 좌표를 리스트로 정리
        self.obj_datas = self.map['layers'][self.layerindex["Object_01"]]['objects']

        # 오브젝트 리스트에 모든 오브젝트저장, [ 이름, x좌표, y좌표, 너비, 높이 ]
        for obj_data in self.obj_datas:
            self.obj_list.append([obj_data["name"], obj_data["x"],self.map_h*32-obj_data["y"],
                                  obj_data["width"], obj_data["height"]])

        # 사각형: left_a = x, bottom_a = y, right_a = x+width , top_a = y+height
        # 중앙: right_a + left_a / 2 , top_a + bottom_a / 2

        for obj_data in self.obj_list:
            self.obj_data_list.append([obj_data[0], obj_data[1], obj_data[2],
                                       obj_data[1] + obj_data[3], obj_data[2] - obj_data[4]])

        All_map.all_obj_data = self.obj_data_list


            # 0 : 이름,  1: 중앙 x, 2: 중앙 y, 3: 너비 x, 4: 높이

        self.canvasWidth = width   # 캔버스 너비
        self.canvasHeight = height # 캔버스 높이
        self.width_dir = 0  # 가로 방향 벡터
        self.height_dir = 0  # 세로 방향 벡터

        self.image_01 = load_image(self.map['tilesets'][0]['image'])
        self.image_02 = load_image(self.map['tilesets'][1]['image'])
        self.image_03 = load_image(self.map['tilesets'][2]['image'])
        self.image_04 = load_image(self.map['tilesets'][3]['image'])
        self.image_05 = load_image(self.map['tilesets'][4]['image'])
        self.image_06 = load_image(self.map['tilesets'][5]['image'])
        self.image_07 = load_image(self.map['tilesets'][6]['image'])

        # self.image = [load_image(self.map['tilesets'][0]['image']),
        #              load_image(self.map['tilesets'][1]['image']),
        #              load_image(self.map['tilesets'][2]['image']),
        #              load_image(self.map['tilesets'][3]['image']),
        #              load_image(self.map['tilesets'][4]['image']),
        #              load_image(self.map['tilesets'][5]['image']),
        #              load_image(self.map['tilesets'][6]['image'])]



    def draw(self):
        mapWidth = self.map["width"]  # 맵 너비
        mapHeight = self.map["height"] # 맵 높이
        data_len = mapWidth * mapHeight

        # 레이어마다 데이터들
        data = [self.map['layers'][self.layerindex["Layer_01"]]['data'],
                self.map['layers'][self.layerindex["Layer_02"]]['data'],
                self.map['layers'][self.layerindex["Layer_03"]]['data']]

        # 각각 타일셋들 ( 맵칩 1 ~ 7 까지 순서대로 저장함 )
        tileset = [self.map['tilesets'][0],self.map['tilesets'][1],self.map['tilesets'][2],
                   self.map['tilesets'][3],self.map['tilesets'][4],self.map['tilesets'][5],
                   self.map['tilesets'][6]]

        tile_width = 32  # 한 타일의 너비 - 고정
        tile_height = 32  # 한 타일의 높이 - 고정

        margin = 0  # 타일간 간격 - 고정
        space = 0 # 타일간 간격 - 고정

        # 타일 칩 마다 열의 개수 (세로가 몇개 인지)
        columns =[tileset[0]['columns'],tileset[1]['columns'],tileset[2]['columns'],
                  tileset[3]['columns'],tileset[4]['columns'],tileset[5]['columns'],
                  tileset[6]['columns']]

        # 타일 칩 마다 행의 개수 ( 가로가 몇개인지 )
        rows = [-(-tileset[0]['tilecount'] // columns[0]), -(-tileset[1]['tilecount'] // columns[1]),
                -(-tileset[2]['tilecount'] // columns[2]), -(-tileset[3]['tilecount'] // columns[3]),
                -(-tileset[4]['tilecount'] // columns[4]), -(-tileset[5]['tilecount'] // columns[5]),
                -(-tileset[6]['tilecount'] // columns[6])]

        # 해당 타일칩의 시작 데이터 1 , 401 , 801, 811, 947, 983, 1383
        firstgid = [tileset[0]['firstgid'], tileset[1]['firstgid'], tileset[2]['firstgid'],
                    tileset[3]['firstgid'], tileset[4]['firstgid'], tileset[5]['firstgid'],
                    tileset[6]['firstgid']]

        # 타일 배열의 시작 좌표
        startx = (tile_width // 2) - self.x % tile_width  # x, y가 0이면 16,16 부터 찍기 시작
        starty = tile_height // 2 - self.x % tile_height

        # x, y가 0이면 16,16 부터 찍기 시작
        #startx = 16 + (All_map.character_x_tile - (self.canvasWidth // 32 // 2))* (tile_width // 2) \
         #        - self.x % tile_width
        #starty = 16 + (All_map.character_y_tile - ((self.canvasHeight+40)//32 // 2))*(tile_height //2) \
          #       - self.y % tile_height



        # 타일 배열의 끝 좌표
        #endx = self.canvasWidth + tile_width // 2  # 816
        #endy = self.canvasHeight + tile_height // 2  # 616

        endx = self.map_w*32 + tile_width // 2  # 816
        endy = self.map_h*32 + tile_height // 2  # 616
        #endx = (All_map.character_x_tile + (self.canvasWidth//32 // 2) )* 32 + tile_width // 2  # 816
        #endy = (All_map.character_y_tile + ((self.canvasHeight+40)//32 // 2))*32 + tile_height // 2  # 616

        #print("맵 좌표: ", self.x, self.y)


        for i in range(3):
            desty = starty
            my = int(self.y // tile_height)  # my는 지금 내가 있는 좌표를 타일로 y번째 순서인지
            #my = int(All_map.character_y_tile - ((self.canvasHeight+40)//32 // 2))
            # 가로를 먼저 찍고 위로 올라가며 찍으니까 y가 끝날때 까지
            while (desty < endy):
                destx = startx
                mx = int(self.x // tile_width)  # mx는 지금 내가 있는 좌표를 타일로 x번째 순서인지
                #mx = int(All_map.character_x_tile - (self.canvasWidth // 32 // 2))

                #print(startx,starty,mx,my)
                # 좌 -> 우로 찍기 시작
                while (destx < endx):
                    index = (mapHeight - my - 1) * mapWidth + mx
                    #index = self.len[i]
                    if index > -1 and index < data_len - 1:
                        tile = data[i][index]  # i번째 레이어 가져옴
                        #print(mx,my)
                        if tile < firstgid[1]:
                            tile = tile - firstgid[0]
                            tx = (tile) % columns[0]  # tx는 타일번호 - 1
                            ty = rows[0] - tile // columns[0] - 1  # y값 순서 바꿔준다.
                            srcx = tx * tile_width
                            srcy = ty * tile_height
                            self.image_01.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)

                        elif tile < firstgid[2]:
                            tile = tile - firstgid[1]
                            tx = (tile) % columns[1]  # tx는 타일번호 - 1
                            ty = rows[1] - tile // columns[1] - 1  # y값 순서 바꿔준다.
                            srcx = tx * tile_width
                            srcy = ty * tile_height
                            self.image_02.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)

                        elif tile < firstgid[3]:
                            tile = tile - firstgid[2]
                            tx = (tile) % columns[2]  # tx는 타일번호 - 1
                            ty = rows[2] - tile // columns[2] - 1  # y값 순서 바꿔준다.
                            srcx = tx * tile_width
                            srcy = ty * tile_height
                            self.image_03.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)

                        elif tile < firstgid[4]:
                            tile = tile - firstgid[3]
                            tx = (tile) % columns[3]  # tx는 타일번호 - 1
                            ty = rows[3] - tile // columns[3] - 1  # y값 순서 바꿔준다.
                            srcx = tx * tile_width
                            srcy = ty * tile_height
                            self.image_04.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)

                        elif tile < firstgid[5]:
                            tile = tile - firstgid[4]
                            tx = (tile) % columns[4]  # tx는 타일번호 - 1
                            ty = rows[4] - tile // columns[4] - 1  # y값 순서 바꿔준다.
                            srcx = tx * tile_width
                            srcy = ty * tile_height
                            self.image_05.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)

                        elif tile < firstgid[6]:
                            tile = tile - firstgid[5]
                            tx = (tile) % columns[5]  # tx는 타일번호 - 1
                            ty = rows[5] - tile // columns[5] - 1  # y값 순서 바꿔준다.
                            srcx = tx * tile_width
                            srcy = ty * tile_height
                            self.image_06.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)

                        else:
                            tile = tile - firstgid[6]
                            tx = (tile) % columns[6]  # tx는 타일번호 - 1
                            ty = rows[6] - tile // columns[6] - 1  # y값 순서 바꿔준다.
                            srcx = tx * tile_width
                            srcy = ty * tile_height
                            self.image_07.clip_draw(srcx, srcy, tile_width, tile_height, destx, desty)

                    # 한칸 찍었으면 -> 로 한칸 이동
                    destx += tile_width
                    mx += 1

                # 한줄 찍었으면 위로 한칸 이동
                desty += tile_height
                my += 1

        #for i in All_map.all_obj_data:
         #  draw_rectangle(i[1], i[2], i[3], i[4])



    def update(self, frame_time):
        distance = TileMap.SCROLL_PPS * frame_time

        if self.width_dir == 1:  # 오른쪽으로 간다
            #self.x = (self.x + distance * self.width_dir)
            pass
        elif self.width_dir == -1:
            self.x = max(0, (self.x + distance * self.width_dir))
        #if self.height_dir == 1:  # 오른쪽으로 간다
        #    self.y = (self.y + distance * self.height_dir)
        #elif self.height_dir == -1:
        #    self.y = (self.y + distance * self.height_dir)

        #print(self.x, self.y)


        #self.x = max(0, (All_map.character_x_tile - (self.canvasWidth // 32 // 2)))
        #self.x = min(40, (All_map.character_x_tile - (self.canvasWidth // 32 // 2)))
        #self.y = max(0,All_map.character_y_tile - ((self.canvasHeight+40)//32 // 2))
        #self.y = min(25,All_map.character_y_tile - ((self.canvasHeight+40)//32 // 2))

        #self.x = (self.x + distance*self.width_dir) % canvasWidth
        #self.y = (self.y + distance*self.height_dir) % canvasHeight
        #print("맵 좌표: ", self.x, self.y)

        #self.x = All_map.character_x // 32
        #self.y = All_map.character_y // 32








    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.width_dir = -1
            elif event.key == SDLK_RIGHT:
                self.width_dir = 1

            elif event.key == SDLK_UP:
                self.height_dir = 1

            elif event.key == SDLK_DOWN:
                self.height_dir = -1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                self.width_dir = 0
            elif event.key == SDLK_RIGHT:
                self.width_dir = 0

            elif event.key == SDLK_UP:
                self.height_dir = 0

            elif event.key == SDLK_DOWN:
                self.height_dir = 0

