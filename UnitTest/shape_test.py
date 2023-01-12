import unittest
import shape_area


class TestArea(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(shape_area.Triangle(10, 5), 25)

    def test_rectangle(self):
        self.assertEqual(shape_area.rectangle(10, 5), 50)

    def test_square(self):
        self.assertEqual(shape_area.square(10), 100)


if __name__ == "__main__":
    unittest.main()