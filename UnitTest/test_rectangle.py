import unittest
import rectangle_perimeter
import sys


class TestArea(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter.get_perimeter(10, 5), 100)

    # @unittest.skip("Temporarily skips error test")
    # @unittest.skipIf(sys.version_info[0]>=3, "Requires Python3 or higher")
    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires windows')
    def test_error(self):
        # self.assertRaises(ValueError, rectangle_perimeter.get_perimeter, 10, 0)
        with self.assertRaises(ValueError):
            rectangle_perimeter.get_perimeter(10,0)
if __name__ == "__main__":
    unittest.main()