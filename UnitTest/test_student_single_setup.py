import unittest
from student import Student


class TestStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetupClass\n")
        cls.stu_1 = Student("Jai", "Ghosh", 25000)
        cls.stu_2 = Student("Sas", "Ghosh", 28000)

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass\n")

    def setUp(self):
        print("\nInside Setup\n")

    def tearDown(self):
        print("\nInside Setup\n")

    def test_mail(self):
        print("test_mail")
        self.assertEqual(self.stu_1.mail, "Jai.Ghosh@xyz.com")
        self.assertEqual(self.stu_2.mail, "Sas.Ghosh@xyz.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.stu_1.fullname, "Jai Ghosh")
        self.assertEqual(self.stu_2.fullname, "Sas Ghosh")

    def test_stipend_hike(self):
        print("test_stipend_hike")
        self.stu_1.apply_hike()
        self.stu_2.apply_hike()

        self.assertEqual(self.stu_1.stipend, 26250)
        self.assertEqual(self.stu_2.stipend, 29400)


if __name__ == "__main__":
    unittest.main()
