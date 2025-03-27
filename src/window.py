from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        self.isWindowRunning = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.isWindowRunning = True

        while self.isWindowRunning:
            self.redraw()

    def close(self):
        self.isWindowRunning = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)

    def draw_cell(self, cell, color):
        cell.draw( color)