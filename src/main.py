from line import Line
from point import Point
from window import Window
from cell import Cell
from maze import Maze

def main():
    window = Window(800, 600)

    maze = Maze(100, 100, 10, 10, 30, 30, window)
    window.wait_for_close()

if __name__ == '__main__':
    main()