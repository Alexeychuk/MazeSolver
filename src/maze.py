from point import Point
from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed = None,
    ):
        if num_rows == 0 or num_cols == 0:
            raise Exception('Maze must have at least one cell')
        if cell_size_x == 0 or cell_size_y == 0:
            raise Exception('cell size cannot be zero')

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        current_left_top_x = self.x1
        current_left_top_y = self.y1
        for i in range(0, self.num_rows):
            row = []
            for j in range(0, self.num_cols):
                row.append(Cell(Point(current_left_top_x,current_left_top_y), Point(current_left_top_x + self.cell_size_x,current_left_top_y + self.cell_size_y),win= self._win, has_top_wall=True, has_left_wall=True, has_bottom_wall=True, has_right_wall=True))
                current_left_top_x += self.cell_size_x

            self._cells.append(row)
            current_left_top_y += self.cell_size_y
            current_left_top_x = self.x1

        for i in range(0, self.num_rows):
                for j in range(0, self.num_cols):
                    self._draw_cell(i,j)
    def _draw_cell(self, i, j):
        self._cells[i][j].draw('black')

        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.00001)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0 ,0)

        self._cells[self.num_rows - 1][self.num_cols - 1].has_bottom_wall = False
        self._draw_cell(self.num_rows - 1 ,self.num_cols - 1)

    def get_neighbor_cells(self, i, j):
        list_to_visit = []
        # from top to left
        if i > 0:
            if not self._cells[i - 1][j].visited:
                list_to_visit.append((i - 1, j))
        if j < self.num_cols - 1:
            if not self._cells[i][j + 1].visited:
                list_to_visit.append((i, j + 1))
        if i < self.num_rows - 1:
            if not self._cells[i + 1][j].visited:
                list_to_visit.append((i + 1,j))
        if j > 0:
            if not self._cells[i][j - 1].visited:
                list_to_visit.append((i, j - 1))

        return list_to_visit

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            list_to_visit = self.get_neighbor_cells(i, j)

            if len(list_to_visit) == 0:
                self._draw_cell(i, j)
                return

            rand = random.randrange(0, len(list_to_visit))
            direction = list_to_visit[rand]

            row_diff = i - direction[0]
            col_diff = j - direction[1]

            if row_diff == -1 and col_diff == 0:
                self._cells[i][j].has_bottom_wall = False
                self._cells[direction[0]][direction[1]].has_top_wall = False
            elif row_diff == 1 and col_diff == 0:
                self._cells[i][j].has_top_wall = False
                self._cells[direction[0]][direction[1]].has_bottom_wall = False
            elif row_diff == 0 and col_diff == -1:
                self._cells[i][j].has_right_wall = False
                self._cells[direction[0]][direction[1]].has_left_wall = False
            elif row_diff == 0 and col_diff == 1:
                self._cells[i][j].has_left_wall = False
                self._cells[direction[0]][direction[1]].has_right_wall = False

            self._draw_cell(i, j)
            self._draw_cell(direction[0], direction[1])

            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        neighbor_cells = self.get_neighbor_cells(i, j)

        for neighbor_cell_location in neighbor_cells:
            neighbor_cell = self._cells[neighbor_cell_location[0]][neighbor_cell_location[1]]
            if neighbor_cell_location[1] == j:
                if (not self._cells[i][j].has_top_wall and not neighbor_cell.has_bottom_wall and not neighbor_cell.visited and i - neighbor_cell_location[0] == 1):
                    self._cells[i][j].draw_move(neighbor_cell)
                    if self._solve_r(neighbor_cell_location[0], neighbor_cell_location[1]):
                        return True
                    else:
                        neighbor_cell.draw_move(self._cells[i][j], undo=True)

                elif (not self._cells[i][j].has_bottom_wall and not neighbor_cell.has_top_wall and not neighbor_cell.visited  and i - neighbor_cell_location[0] == -1):
                    self._cells[i][j].draw_move(neighbor_cell)
                    if self._solve_r(neighbor_cell_location[0], neighbor_cell_location[1]):
                        return True
                    else:
                        neighbor_cell.draw_move(self._cells[i][j], undo=True)

            if neighbor_cell_location[0] == i:
                if (not self._cells[i][j].has_right_wall and not neighbor_cell.has_left_wall and not neighbor_cell.visited and j - neighbor_cell_location[1] == -1):
                    self._cells[i][j].draw_move(neighbor_cell)
                    if self._solve_r(neighbor_cell_location[0], neighbor_cell_location[1]):
                        return True
                    else:
                        neighbor_cell.draw_move(self._cells[i][j], undo=True)


                elif (not self._cells[i][j].has_left_wall and not neighbor_cell.has_right_wall and not neighbor_cell.visited and j - neighbor_cell_location[1] == 1):
                    self._cells[i][j].draw_move(neighbor_cell)
                    if self._solve_r(neighbor_cell_location[0], neighbor_cell_location[1]):
                        return True
                    else:
                        neighbor_cell.draw_move(self._cells[i][j], undo=True)

        return False



