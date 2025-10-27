"""
Student: David Wilson
Instructor: Tim McMichael
Date Modified: 10/26/2025
Class: CIS256
Module 04 Python Programming Project

Part B of B

File Name: student_grade.py
Additional File(s): student_grade_demo.py, test_student_grade.py, README.md

This Python program contains a StudentGrade class for creating a new student
grade object. It will be initialized and tested separately in the demo program
file of the same name. Another program is also included for unit testing the
class with valid and invalid data.
"""

# Start of program

# Import statements
from datetime import date
import sys


class StudentGrade:
    """
    This class contains all the necessary attributes and methods related to
    keeping track of a student's running grade percentage and total points
    throughout a semester.
    """

    def __init__(self, student_name, pts_earned, pts_possible):
        """
        Initializes a new Student object with attributes to represent their
        current grade.

        Parameters (Args):
        1.) student_name (str): The current student's name receiving the grade.
        2.) pts_earned (float): The student's total earned points at this point.
        3.) pts_possible (int): The total possible points in the course to this point.
        """
        self.__student_name = student_name  # Encapsulated student_name attribute
        self.__points_earned = pts_earned  # Encapsulated points_earned attribute
        self.__points_possible = pts_possible  # Encapsulated points_possible attribute

    # Read access methods (accessors) for each attribute
    # Some are added methods for __str__ to display a formatted string with all data
    def get_student_name(self) -> str:
        return self.__student_name

    def get_points_earned(self) -> float:
        return self.__points_earned

    def get_points_possible(self) -> int:
        return self.__points_possible

    # Additional accessor methods to determine the student's overall percentage
    # and letter grade
    def get_percentage_grade(self) -> float:
        if not self.__points_possible == 0:  # Effectively prevents a ZeroDivisionError
            return (self.__points_earned / self.__points_possible) * 100
        else:
            return 100

    def get_letter_grade(self) -> str:
        grade_percent = self.get_percentage_grade()
        if grade_percent <= 100:
            if grade_percent >= 90:
                return "A"
            elif grade_percent <= 89.9:
                if grade_percent >= 80:
                    return "B"
                elif grade_percent <= 79.9:
                    if grade_percent >= 70:
                        return "C"
                    elif grade_percent <= 69.9:
                        if grade_percent >= 60:
                            return "D"
                        elif grade_percent <= 59.9:
                            if grade_percent >= 0:
                                return "F"
                            else:
                                return "N/A"
        else:
            return "N/A"

    # Write access method (mutator) for ONLY the student_name attribute
    def set_student_name(self, full_name):
        space_char = " "  # Default separator for first and last name(s)
        space_index = 0  # Indexes for spaces in student_name string set accordingly
        last_space = -1
        if full_name.count(space_char) <= 1:
            space_index = full_name.find(space_char)
        else:
            space_index = full_name.find(space_char)  # First occurrence of space
            last_space = full_name.rfind(space_char)  # Last occurrence of space
        if not len(full_name) >= 7:
            raise ValueError(
                "Please enter a valid student's full name (first "
                + "letters capitalized).\nPlease try again."
            )
        elif not space_char in full_name:
            raise ValueError(
                "The student's full name must be separated by one or\n"
                + "more spaces. Please try again."
            )
        elif not full_name[0].isupper():
            raise ValueError(
                "The first letters of the student's first and last "
                + "name\nmust be capitalized. Please try again."
            )
        elif not full_name[space_index + 1].isupper():
            raise ValueError(
                "The first letters of the student's first and last "
                + "name\nmust be capitalized. Please try again."
            )
        elif not full_name[0:space_index].isalpha():
            raise ValueError(
                "The student's full name may not contain numbers\nor "
                + "special characters. Please try again."
            )
        elif not full_name[space_index + 1 : last_space].isalpha():
            raise ValueError(
                "The student's full name may not contain numbers\nor "
                + "special characters. Please try again."
            )
        else:
            self.__student_name = full_name

    # Total point accumulation manipulation methods to add an assignment score
    # or extra credit for the student
    def add_assignment_score(self, pts_earned, pts_possible):
        if not pts_earned >= 0:
            raise ValueError(
                "The entered assignment score can't be negative. Please try again."
            )
        elif not pts_possible >= 1:
            raise ValueError(
                "The total number of possible points for the assignment\n"
                + "must be greater than zero. Please try again."
            )
        elif not pts_earned <= pts_possible:
            raise ValueError(
                "The entered assignment score may not exceed the total\n"
                + "number of possible points for the assignment. Please "
                + "try again."
            )
        else:
            self.__points_earned += pts_earned
            self.__points_possible += pts_possible

    def add_extra_credit(self, extra_pts):
        if not extra_pts >= 1:
            raise ValueError(
                "Extra credit points must be greater than zero. Please try again."
            )
        elif not extra_pts <= self.__points_possible - self.__points_earned:
            raise ValueError(
                "Extra credit points may not exceed the total number\nof "
                + "possible points in the course. Please try again."
            )
        else:
            self.__points_earned += extra_pts

    """
    A __str__ method that invokes when the class is called in a print() statement.
    It returns a string representing the student's name, total points accumulated
    out of points possible, as well as their current percentage and letter grade.
    You can also specify a docstring to print more than one line.
    """

    def __str__(self) -> str:
        grade_percent = self.get_percentage_grade()
        letter_grade = self.get_letter_grade()
        if (grade_percent % 1 == 0) and (self.__points_earned % 1 == 0):
            # The modulo operator gives the remainder of division
            # Checks to confirm grade_percent and pts_earned are whole numbers
            return f"""
            \t\t\t\t\t\b\bStudent Name: {self.get_student_name()}
            \n\t\t\t\t\t\t\b\bPoints Earned: {self.get_points_earned():.0F} out of {self.get_points_possible()}
            \n\t\t\t\t\t\t\b\bPercentage Grade: {grade_percent:.0F}%
            \n\t\t\t\t\t\t\b\bLetter Grade: {letter_grade}
            """
        elif (grade_percent % 1 > 0) and (self.__points_earned % 1 > 0):
            return f"""
            \t\t\t\t\t\b\bStudent Name: {self.get_student_name()}
            \n\t\t\t\t\t\t\b\bPoints Earned: {self.get_points_earned():.1F} out of {self.get_points_possible()}
            \n\t\t\t\t\t\t\b\bPercentage Grade: {grade_percent:.1F}%
            \n\t\t\t\t\t\t\b\bLetter Grade: {letter_grade}
            """
        elif grade_percent % 1 > 0:
            return f"""
            \t\t\t\t\t\b\bStudent Name: {self.get_student_name()}
            \n\t\t\t\t\t\t\b\bPoints Earned: {self.get_points_earned():.0F} out of {self.get_points_possible()}
            \n\t\t\t\t\t\t\b\bPercentage Grade: {grade_percent:.1F}%
            \n\t\t\t\t\t\t\b\bLetter Grade: {letter_grade}
            """
        else:
            return f"""
            \t\t\t\t\t\b\bStudent Name: {self.get_student_name()}
            \n\t\t\t\t\t\t\b\bPoints Earned: {self.get_points_earned():.1F} out of {self.get_points_possible()}
            \n\t\t\t\t\t\t\b\bPercentage Grade: {grade_percent:.0F}%
            \n\t\t\t\t\t\t\b\bLetter Grade: {letter_grade}
            """


# Begin program execution
if __name__ == "__main__":  # Checks to confirm this is the active program
    print(
        "—" * 120
        + "\n"
        + format(
            "Module 04 Python Programming Exercise(s): Student Grade Class", "^120"
        )
        + "\n"
        + format(
            "Week 5 Project: Part B — Student Grade Class — Grade Calculator", "^120"
        )
        + "\n"
        + format("Written By David Wilson for Tim McMichael's Python Class", "^120")
        + "\n"
        + format(
            "Date Modified: " + format(date(2025, 10, 26).strftime("%m/%d/%Y")), "^120"
        )
        + "\n"
        + "—" * 120
    )
    input(
        "\nThe student grade class file was run directly.\nPlease run the "
        + "student_grade_demo program from\nthe local directory.\n\nPress ENTER "
        + "to exit the program >> "
    )
    sys.exit()
