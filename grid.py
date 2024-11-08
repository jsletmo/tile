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
        grid_size = 11
        half_grid_size = grid_size // 2  # This will be 5 for an 11x11 grid
        temp_grid = []
        
        # Corrected calulation for the top row to ensure it doesn't go out-of-bounds
        toprow = max(0, player_y - half_grid_size)
        
        for i in range(grid_size):
            current_row_idx = toprow + i
            
            # Check if the current row is within the bounds of the main grid
            if 0 <= current_row_idx < len(self._grid):
                entire_row = self._grid[current_row_idx]
                
                # Corrected calculations for the starting and ending indices of the slicing
                left_bound = max(0, player_x - half_grid_size)
                right_bound = min(len(entire_row), player_x + half_grid_size + 1)
                
                shortened_row = entire_row[left_bound:right_bound]
                
                # Pad shortened_row if it's less than grid_size
                if len(shortened_row) < grid_size:
                    # If left_bound is 0, we pad on the right side, otherwise pad on the left
                    left_padding = ['3'] * (grid_size - len(shortened_row)) if left_bound > 0 else []
                    right_padding = ['3'] * (grid_size - len(shortened_row)) if left_bound == 0 else []
                    
                    shortened_row = left_padding + shortened_row + right_padding
            else:
                # If the row index (current_row_idx) is out of bounds, add a full 'out-of-bounds' row
                shortened_row = ['3'] * grid_size
            
            temp_grid.append(shortened_row)
            
        return temp_grid



            



if __name__ == "__main__":
    grid = Grid("map.txt")
    print(grid.create_visual_grid(6, 6))