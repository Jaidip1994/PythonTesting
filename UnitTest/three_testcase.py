import unittest


class Testing(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('beta'.upper(), 'BETA')

    def test_boolean(self):
        self.assertEqual(True, True)

    def test_isupper(self):
        self.assertTrue('BETA'.isupper())
        self.assertFalse('BETA'.islower())


if __name__ == "__main__":
    unittest.main()
