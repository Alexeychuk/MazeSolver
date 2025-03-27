from line import Line
from point import Point
from window import Window
from cell import Cell
from maze import Maze

def main():
    window = Window(1700, 1200)

    maze = Maze(100, 100, 20, 20, 30, 30, window)
    maze.solve()
    window.wait_for_close()

if __name__ == '__main__':
    main()