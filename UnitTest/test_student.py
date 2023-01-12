import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_mail(self):
        stu_1 = Student("Jai", "Ghosh", 25000)
        stu_2 = Student("Sas", "Ghosh", 28000)

        self.assertEqual(stu_1.mail, "Jai.Ghosh@xyz.com")
        self.assertEqual(stu_2.mail, "Sas.Ghosh@xyz.com")

        stu_1.first = "Joy"
        stu_2.first = "Sash"

        self.assertEqual(stu_1.mail, "Joy.Ghosh@xyz.com")
        self.assertEqual(stu_2.mail, "Sash.Ghosh@xyz.com")

    def test_fullname(self):
        stu_1 = Student("Jai", "Ghosh", 25000)
        stu_2 = Student("Sas", "Ghosh", 28000)

        self.assertEqual(stu_1.fullname, "Jai Ghosh")
        self.assertEqual(stu_2.fullname, "Sas Ghosh")

        stu_1.first = "Joy"
        stu_2.first = "Sash"

        self.assertEqual(stu_1.fullname, "Joy Ghosh")
        self.assertEqual(stu_2.fullname, "Sash Ghosh")

    def test_stipend_hike(self):
        stu_1 = Student("Jai", "Ghosh", 25000)
        stu_2 = Student("Sas", "Ghosh", 28000)

        stu_1.apply_hike()
        stu_2.apply_hike()

        self.assertEqual(stu_1.stipend, 26250)
        self.assertEqual(stu_2.stipend, 29400)


if __name__ == "__main__":
    unittest.main()
