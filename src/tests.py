import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_one_row(self):
        num_cols = 100
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    def test_maze_create_cells_one_column(self):
        num_cols = 100
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_exception_on_zero_cells(self):
        num_cols = 0
        num_rows = 100
        with self.assertRaises(Exception) as context:
            Maze(0, 0, num_rows, num_cols, 10, 10)

    def test_maze_exception_on_zero_cell_size(self):
        num_cols = 10
        num_rows = 10
        with self.assertRaises(Exception) as context:
            Maze(0, 0, num_rows, num_cols, 0, 10)

    def test_maze_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall,
            False,
        )
    def test_reset_visited(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        for i in range(0, m1.num_rows):
            for j in range(0, m1.num_cols):
                if m1._cells[i][j].visited:
                    self.fail()
