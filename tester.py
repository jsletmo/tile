class Grid:
    def __init__(self, gridfile):
        self._file = self.open_file(gridfile)
        self._grid = []
        self.create_grid()
        visual_grid = []
        
    def open_file(self, file):
        temp_list = []
        with open(file) as my_file:
            for i in my_file:
                line = i.strip()
                temp_list.append(line)
        return temp_list

    def return_worldgrid(self):
        return self._grid
                
    def create_grid(self):
        for rows in self._file:
            self._grid.append(self.create_row(rows))


    def create_row(self, filestring):
            row = []
            tiles = filestring.split(",")
            for tile in tiles:
                temp = tile
                row.append(temp)
            return row
        
    def create_visual_grid(self, player_y, player_x):
        start_y = player_y - 6
        end_y = player_y + 5
        start_x = player_x - 6
        end_x = player_x + 5
        temp_grid = []
        temp_row = []
        
        for row in self._grid[start_y:end_y]:
            temp_row = row[start_x:end_x]
            temp_grid.append(temp_row)

        return temp_grid



            



if __name__ == "__main__":
    grid = Grid("map.txt")
    print(grid.create_visual_grid(6, 6))
    print(len(grid.create_visual_grid(6, 6)))