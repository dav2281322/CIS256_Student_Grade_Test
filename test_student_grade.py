"""
David Wilson
Module 07 Lab Programming Assignment

Part A

File Name: test_student_grade.py

This is a Python module containing multiple test cases of relevance, for testing
the StudentGrade class in the student_grade_class_demo program. A suite of at
least 5 different test cases (assertions) will be evaluated, each presenting a
pass/fail prompt when the program is run.
"""

# Start of program

# Import statements
import unittest
from student_grade import *


class TestStudentGrade(unittest.TestCase):
    """
    A testing class solely for testing a number of StudentGrade class methods.
    """

    def setUp(self):
        self.student1 = StudentGrade("John Smith", 899, 1000)
        # self.student1.set_student_name("Example")
        self.student1.set_student_name("Example Student")
        self.student2 = StudentGrade("David Wilson", 987, 1000)
        self.student2.set_student_name("David Edward")
        self.student3 = StudentGrade("Test Student", -1, 1000)
        # self.student3.set_student_name("Test A")
        self.student3.set_student_name("Test A Student")
        self.student4 = StudentGrade("Tim McMichael", 2001, 2000)
        # self.student4.set_student_name("TimothyJohn")
        self.student4.set_student_name("Timothy John")
        self.student5 = StudentGrade("Bill Stewart", 2000, 2000)
        self.student5.set_student_name("William Stewart")

    def test_get_student_name(self):
        # self.assertNotEqual(self.student1.get_student_name(), "Example")
        self.assertNotEqual(self.student1.get_student_name(), "John Smith")
        self.assertEqual(self.student2.get_student_name(), "David Edward")
        # self.assertNotEqual(self.student3.get_student_name(), "Test A")
        self.assertNotEqual(self.student3.get_student_name(), "Test Student")
        # self.assertNotEqual(self.student4.get_student_name(), "TimothyJohn")
        self.assertNotEqual(self.student4.get_student_name(), "Tim McMichael")
        self.assertEqual(self.student5.get_student_name(), "William Stewart")

    def test_get_percentage_grade(self):
        self.assertEqual(self.student1.get_percentage_grade(), 89.9)
        self.assertEqual(self.student2.get_percentage_grade(), 98.7)
        self.assertEqual(self.student3.get_percentage_grade(), -0.1)
        self.assertEqual(self.student4.get_percentage_grade(), 100.05)
        self.assertEqual(self.student5.get_percentage_grade(), 100.0)

    def test_get_letter_grade(self):
        self.assertEqual(self.student1.get_letter_grade(), "B")
        self.assertEqual(self.student2.get_letter_grade(), "A")
        self.assertEqual(self.student3.get_letter_grade(), "N/A")
        self.assertEqual(self.student4.get_letter_grade(), "N/A")
        self.assertEqual(self.student5.get_letter_grade(), "A")

    def test_add_assignment_score(self):
        self.student1.add_assignment_score(75, 75)
        self.assertEqual(self.student1.get_points_earned(), 974)
        self.assertEqual(self.student1.get_points_possible(), 1075)
        self.assertAlmostEqual(self.student1.get_percentage_grade(), 90.6, places=1)
        self.assertEqual(self.student1.get_letter_grade(), "A")
        self.student2.add_assignment_score(85, 100)
        self.assertEqual(self.student2.get_points_earned(), 1072)
        self.assertEqual(self.student2.get_points_possible(), 1100)
        self.assertAlmostEqual(self.student2.get_percentage_grade(), 97.5, places=1)
        self.assertEqual(self.student2.get_letter_grade(), "A")
        self.student3.add_assignment_score(50, 100)
        self.assertEqual(self.student3.get_points_earned(), 49)
        self.assertEqual(self.student3.get_points_possible(), 1100)
        self.assertAlmostEqual(self.student3.get_percentage_grade(), 4.5, places=1)
        self.assertEqual(self.student3.get_letter_grade(), "F")
        # self.student4.add_assignment_score(-1, 0)
        self.assertEqual(self.student4.get_points_earned(), 2001)
        self.assertEqual(self.student4.get_points_possible(), 2000)
        self.assertEqual(self.student4.get_percentage_grade(), 100.05)
        self.assertEqual(self.student4.get_letter_grade(), "N/A")
        self.student5.add_assignment_score(150, 200)
        self.assertEqual(self.student5.get_points_earned(), 2150)
        self.assertEqual(self.student5.get_points_possible(), 2200)
        self.assertAlmostEqual(self.student5.get_percentage_grade(), 97.7, places=1)
        self.assertEqual(self.student5.get_letter_grade(), "A")

    def test_add_extra_credit(self):
        pass


# Begin program execution
print(
    "—" * 120
    + "\n"
    + format("Testing StudentGrade Class: Valid & Invalid Data Test Cases", "^120")
    + "\n"
    + format("Written By David Wilson for Tim McMichael's Python Class", "^120")
    + "\n"
    + format("Week 8 Practice: Python Unit Testing", "^120")
    + "\n"
    + format("Module 07: Part A — Former Project Unit Testing Demo", "^120")
    + "\n"
    + format(
        "Date Modified: " + format(date(2025, 10, 27).strftime("%m/%d/%Y")), "^120"
    )
    + "\n"
    + "—" * 120
    + "\n"
)
if __name__ == "__main__":  # Checks to confirm this is the active program
    unittest.main()
    sys.exit()
# End of program
