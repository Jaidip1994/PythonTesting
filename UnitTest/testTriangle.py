import unittest
import triangle_area


class TestArea(unittest.TestCase):
    def test_triangle(self):
        result = triangle_area.Triangle(10, 5)
        self.assertEqual(result, 25)


if __name__ == "__main__":
    unittest.main()
