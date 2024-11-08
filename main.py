import pygame as pg
from tester import Grid

pg.init()

window_res = (352, 352)
window = pg.display.set_mode(window_res)
clock = pg.time.Clock()
running = True


class Tile:
    def __init__(self, pos, image, id):
        self._sprite_img = image.subsurface(pos)
        self._sprite_id = id
    
    def display_tile(self, pos):
        window.blit(self._sprite_img, pos)

    def __eq__(self, x):
        return self._sprite_id == x

# class Grid:
#     def __init__(self, gridfile):
#         self._file = self.open_file(gridfile)
#         self._grid = []
#         self.create_grid()
#         visual_grid = []
        
#     def open_file(self, file):
#         temp_list = []
#         with open(file) as my_file:
#             for i in my_file:
#                 line = i.strip()
#                 temp_list.append(line)
#         return temp_list

#     def return_worldgrid(self):
#         return self._grid
                
#     def create_grid(self):
#         for rows in self._file:
#             self._grid.append(self.create_row(rows))


#     def create_row(self, filestring):
#             row = []
#             tiles = filestring.split(",")
#             for tile in tiles:
#                 temp = tile
#                 row.append(temp)
#             return row
    
#     def create_visual_grid(self):
#         temp_grid = []
#         shortend_row = []
#         for space in range(11):
#             shortend_row = self._grid[player_y]
            





img_tiles = pg.image.load("tiles.png").convert_alpha()
all_player_sprites = pg.image.load("player_sprites.png").convert_alpha()
player_sprite = all_player_sprites.subsurface((0,0,230, 300))
player_sprite = pg.transform.smoothscale(player_sprite,(32, 32)).convert_alpha()
player_x = 6
player_y = 6



grass = Tile((0,0,32,32), img_tiles, "1")
plant = Tile((0,64,32,32),img_tiles, "0")
barrier = Tile((224,0,32,32),img_tiles, "3")
boat1 = Tile((224,320,32,32),img_tiles, "11")
boat2 = Tile((224,352,32,32),img_tiles, "12")
tiles = [grass, plant]


def display_screen(map):
    grid = map
    counter_row = 0
    for row in grid:
        counter_tile = 0
        for tile in row:
            tile_check(tile, (counter_tile*32,counter_row*32))
            counter_tile += 1
        counter_row += 1

def tile_check(type, pos):
    if grass == type:
        grass.display_tile(pos)
    elif plant == type:
        plant.display_tile(pos)
    elif boat1 == type:
        boat1.display_tile(pos)
    elif boat2 == type:
        boat2.display_tile(pos)
    else:
        barrier.display_tile(pos)




world_grid = Grid("map.txt")
print(world_grid.return_worldgrid())

 

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False
        if event.type == pg.KEYDOWN:    #Detection for keypress for controls
            if event.key == pg.K_a:
                player_x += 1
            if event.key == pg.K_d:
                player_x -= 1
            if event.key == pg.K_w:
                player_y -=1
            if event.key == pg.K_s:
                player_y += 1

  



    display_screen(world_grid.create_visual_grid(player_y, player_x))
    window.blit(player_sprite,(160, 160))           #Place player in the middle of the screen




    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()