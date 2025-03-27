from point import Point

class Cell:
    def __init__(self,  top_left_point, bottom_right_point, win = None, has_left_wall = True, has_right_wall= True, has_top_wall= True, has_bottom_wall= True,):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = top_left_point.x
        self._x2 = bottom_right_point.x
        self._y1 = top_left_point.y
        self._y2 = bottom_right_point.y
        self._win = win
        self.visited = False
        self.center_point = Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2)

    def __repr__(self):
        return f"Cell(top_left_point={self._x1}, {self._y1}, bottom_right_point={self._x2}, {self._y2}), has_left_wall={self.has_left_wall}, has_right_wall={self.has_right_wall}, has_top_wall={self.has_top_wall}, has_bottom_wall={self.has_bottom_wall})"

    def draw(self,  color):
        if self._win is None:
            return

        self._win.canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill=color if self.has_left_wall else 'white', width=2)
        self._win.canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill=color if self.has_right_wall else 'white', width=2)
        self._win.canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill=color if self.has_top_wall else 'white', width=2)
        self._win.canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill=color if self.has_bottom_wall else 'white', width=2)

    def draw_move(self,  to_cell, undo=False):
        color = 'red' if undo else 'gray'

        self._win.canvas.create_line(self.center_point.x, self.center_point.y, to_cell.center_point.x, to_cell.center_point.y, fill=color, width=2)