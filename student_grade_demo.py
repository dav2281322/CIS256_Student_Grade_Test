"""
Student: David Wilson
Instructor: Tim McMichael
Date Modified: 10/26/2025
Class: CIS256
Module 04 Python Programming Project

Part B of B

File Name: cis256_mod04_student_grade_class_demo.py
Additional File(s): student_grade.py, test_student_grade.py, README.md

This Python program demonstrates the use of a class titled StudentGrade,
in order to maintain a running percentage and assigned letter grade for
a student throughout a course. Its main attributes consist of the student's
name, total points earned, and total points possible. User input is not
required, although I will still include it to test all functionality of the
class with different input values.

The menu choices for navigating and using this program include:
A.) Set Student Name
B.) Add Assignment Score
C.) Add Extra Credit
D.) View Current Grade
E.) Quit Grading
"""

# Start of program

# Import statements
from student_grade import *

# Global variables/constant declarations
valid_input = False
end_function = False
student_count = 0  # Used to keep track of how many students have been recorded
user_choice = ""


# Main method declaration
# Holds the main program logic and tests the class's functionality with input
def main() -> None:
    global valid_input, end_function, student_count
    menu_options = [
        "set student name",
        "add assignment score",
        "add extra credit",
        "view current grade",
        "quit grading",
    ]
    new_student = ""
    old_student = ""
    pts_earned = 0  # The total number of earned points on a given assignment
    pts_extra = 0
    pts_possible = 0  # The total number of possible points on a given assignment
    student_info = get_student_info()  # Initialize a new student grade object
    if student_info is not None:
        student_count += 1
        print(
            "\n\n"
            + "+=" * 60
            + "\n\n"
            + format("Current Grade for Student " + format(student_count) + ":", "^120")
            + "\n\n"
            + "+=" * 60
            + "\n"
            + str(student_info)
            + "\n"
            + "—" * 120
        )
        print("\nNew student info was created successfully!")
        input("\nPress ENTER to continue >> ")
        print("\n" + "—" * 120)
        if end_function is True:
            end_function = False
        while not end_function:
            # Display all available options in the form of a menu
            print(
                "\nWhat would you like to do? (Select one from the following options):"
            )
            for index, choice in enumerate(menu_options):
                if index < 1:
                    select_char = "A"
                    print(f"\n{select_char}.) {choice.title()}")
                elif index == 1:
                    select_char = "B"
                    print(f"\n{select_char}.) {choice.title()}")
                elif index == 2:
                    select_char = "C"
                    print(f"\n{select_char}.) {choice.title()}")
                elif index == 3:
                    select_char = "D"
                    print(f"\n{select_char}.) {choice.title()}")
                else:
                    select_char = "E"
                    print(f"\n{select_char}.) {choice.title()}")
            # Get valid menu selection input option from user
            menu_choice = get_menu_selection(
                "\nEnter your selection (e.g. 'A' for first option, etc.) >> ",
                student_info.get_student_name(),
                menu_options,
            )
            if menu_choice == menu_options[-1]:  # An index of -1 returns last element
                end_function = True
            else:
                if menu_choice == menu_options[0]:
                    old_student = student_info.get_student_name()  # Original name
                    valid_input = False
                    while not valid_input:
                        try:
                            valid_input = True
                            new_student = input(
                                "\nEnter the new name for "
                                + f"{old_student} (e.g. 'John Smith') "
                                + ">> "
                            ).strip()
                            student_info.set_student_name(new_student)  # New name
                        except ValueError as name_input_err:
                            valid_input = False
                            print(f"\nError: {name_input_err}")
                            print("\n" + "—" * 120)
                        else:
                            print(
                                f"\n{old_student}'s name was successfully changed "
                                + f"to {student_info.get_student_name()}!"
                            )
                            input("\nPress ENTER to continue >> ")
                            print("\n" + "—" * 120)
                elif menu_choice == menu_options[1]:
                    valid_input = False
                    while not valid_input:
                        try:
                            valid_input = True
                            pts_earned = float(
                                input(
                                    "\nEnter the total points earned "
                                    + "on the assignment\n(as a "
                                    + "decimal or whole number) >> "
                                ).strip()
                            )
                            pts_possible = int(
                                input(
                                    "\nEnter the number of points "
                                    + "possible for the assignment "
                                    + "(e.g. 200) >> "
                                ).strip()
                            )
                            student_info.add_assignment_score(pts_earned, pts_possible)
                        except ValueError as pts_input_err:
                            if "negative" in str(pts_input_err):
                                valid_input = False
                                print(f"\nError: {pts_input_err}")
                                print("\n" + "—" * 120)
                            elif "zero" in str(pts_input_err):
                                valid_input = False
                                print(f"\nError: {pts_input_err}")
                                print("\n" + "—" * 120)
                            elif "exceed" in str(pts_input_err):
                                valid_input = False
                                print(f"\nError: {pts_input_err}")
                                print("\n" + "—" * 120)
                            else:
                                # A different type of value was entered
                                valid_input = False
                                print(
                                    f"\nError: Invalid number of points specified "
                                    + "for assignment!\nPlease try again."
                                )
                                print(f"\nHere's the error details: {pts_input_err}.")
                                print("\n" + "—" * 120)
                        except Exception as ex:
                            valid_input = False
                            print(
                                "\nError: Something went wrong while trying to "
                                + "process the grade\nfor this assignment. "
                                + "Please close the program and try again."
                            )
                            print(f"\nHere's the error details: {ex}.")
                            print("\n" + "—" * 120)
                        else:
                            print(
                                f"\n{student_info.get_student_name()}'s assignment "
                                + "score was added successfully!"
                            )
                            input("\nPress ENTER to continue >> ")
                            print("\n" + "—" * 120)
                elif menu_choice == menu_options[2]:
                    valid_input = False
                    while not valid_input:
                        try:
                            valid_input = True
                            pts_extra = int(
                                input(
                                    "\nEnter the number of extra credit "
                                    + "points to be granted\n(e.g. 15) "
                                    + ">> "
                                ).strip()
                            )
                            student_info.add_extra_credit(pts_extra)
                        except ValueError as extra_pts_input_err:
                            if "zero" in str(extra_pts_input_err):
                                valid_input = False
                                print(f"\nError: {extra_pts_input_err}")
                                print("\n" + "—" * 120)
                            elif "exceed" in str(extra_pts_input_err):
                                valid_input = False
                                print(f"\nError: {extra_pts_input_err}")
                                print("\n" + "—" * 120)
                            else:
                                # A different type of value was entered
                                valid_input = False
                                print(
                                    "\nError: Invalid extra credit points specified!"
                                    + " Please try again."
                                )
                                print(
                                    f"\nHere's the error details: {extra_pts_input_err}."
                                )
                                print("\n" + "—" * 120)
                        else:
                            print(
                                f"\n{student_info.get_student_name()}'s extra "
                                + "credit points were added successfully!"
                            )
                            input("\nPress ENTER to continue >> ")
                            print("\n" + "—" * 120)
                else:
                    print(
                        "\n\n"
                        + "+=" * 60
                        + "\n\n"
                        + format(
                            "Updated Grade for Student " + format(student_count) + ":",
                            "^120",
                        )
                        + "\n\n"
                        + "+=" * 60
                        + "\n"
                        + str(student_info)
                        + "\n"
                        + "—" * 120
                    )
                    input("\nPress ENTER to continue >> ")
                    print("\n" + "—" * 120)
    else:
        print(
            "\nError: Something went wrong while processing your student data."
            + "\nPlease close the program and try again."
        )
        print("\n" + "—" * 120)
        input("\nPress ENTER to exit the demo >> ")
    return


# Secondary method declaration (will request the user for all necessary class info)
def get_student_info() -> StudentGrade:
    global valid_input
    space_char = " "
    space_index = 0
    last_space = -1
    pts_earned = None  # Initialize the pts_earned variable to prevent UnboundLocalError
    pts_possible = 0
    if valid_input is True:
        valid_input = False
    while not valid_input:
        try:
            valid_input = True
            student_name = input(
                "\nEnter the student's full name (e.g. 'John Smith') >> "
            ).strip()
            if student_name.count(space_char) <= 1:
                space_index = student_name.find(space_char)
            else:
                space_index = student_name.find(space_char)
                last_space = student_name.rfind(space_char)
            if not len(student_name) >= 7:
                valid_input = False
                raise ValueError(
                    "Please enter a valid student's full name (first "
                    + "letters capitalized).\nPlease try again."
                )
            elif not space_char in student_name:
                valid_input = False
                raise ValueError(
                    "The student's full name must be separated by one "
                    + "or\nmore spaces. Please try again."
                )
            elif not student_name[0].isupper():
                valid_input = False
                raise ValueError(
                    "The first letters of the student's first and last "
                    + "name\nmust be capitalized. Please try again."
                )
            elif not student_name[space_index + 1].isupper():
                valid_input = False
                raise ValueError(
                    "The first letters of the student's first and last "
                    + "name\nmust be capitalized. Please try again."
                )
            elif not student_name[0:space_index].isalpha():
                valid_input = False
                raise ValueError(
                    "The student's full name may not contain numbers\nor "
                    + "special characters. Please try again."
                )
            elif not student_name[space_index + 1 : last_space].isalpha():
                valid_input = False
                raise ValueError(
                    "The student's full name may not contain numbers\nor "
                    + "special characters. Please try again."
                )
            else:
                pass
        except ValueError as name_input_err:
            print(f"\nError: {name_input_err}")
            print("\n" + "—" * 120)
    valid_input = False
    while not valid_input:
        try:
            valid_input = True
            pts_earned = float(
                input(
                    "\nEnter his/her total points earned (as a "
                    + "decimal or whole number) >> "
                ).strip()
            )
            if not isinstance(pts_earned, float):
                # Verifies whether or not user's input contains ONLY numbers
                # and a decimal place (if applicable)
                valid_input = False
                raise ValueError
            else:
                if not pts_earned >= 0:
                    valid_input = False
                    raise ValueError(
                        "The total number of points earned can't be "
                        + "negative.\nPlease try again."
                    )
                else:
                    pass
        except ValueError as pts_earned_input_err:
            if "negative" in str(pts_earned_input_err):
                print(f"\nError: {pts_earned_input_err}")
                print("\n" + "—" * 120)
            else:
                print(
                    "\nError: Invalid number of points earned specified! Please try "
                    + "again."
                )
                print(f"\nHere's the error details: {pts_earned_input_err}.")
                print("\n" + "—" * 120)
        except Exception as ex:
            # A different type of error occurred
            valid_input = False
            print(
                "\nError: Something went wrong while trying to process this student's"
                + "\ngrade info. Please close the program and try again."
            )
            print(f"\nHere's the error details: {ex}.")
            print("\n" + "—" * 120)
    valid_input = False
    while not valid_input:
        try:
            valid_input = True
            pts_possible = int(
                input(
                    "\nEnter the total points possible to this point "
                    + "(e.g. 500) >> "
                ).strip()
            )
            if not pts_possible >= pts_earned:
                valid_input = False
                raise ValueError(
                    "The total number of points possible must be higher "
                    + "than\nthe total number of points earned. Please "
                    + "try again."
                )
            else:
                print("\n" + "—" * 120)
                print(
                    f"\nThank you! Now preparing to store {student_name}'s grade "
                    + "totals\nin main memory. I will also use this data to "
                    + "collectively\ndetermine their overall grade, as a "
                    + "percentage and a letter\ngrade (i.e. A-F)."
                )
                input("\nPress ENTER to continue >> ")
        except ValueError as pts_possible_input_err:
            if "higher" in str(pts_possible_input_err):
                print(f"\nError: {pts_possible_input_err}")
                print("\n" + "—" * 120)
            else:
                valid_input = False
                print(
                    "\nError: Invalid total number of possible points specified!"
                    + "\nPlease try again."
                )
                print(f"\nHere's the error details: {pts_possible_input_err}.")
                print("\n" + "—" * 120)
    return StudentGrade(student_name, pts_earned, pts_possible)


# This function prompts the user for a selection and validates their input
# against a list of options. The test is case-insensitive.
def get_menu_selection(user_prompt, student_name, menu_options) -> str:
    global valid_input
    if valid_input is True:
        valid_input = False  # Reset the valid_input flag value to test again
    while not valid_input:
        print("\n" + "—" * 120)
        valid_input = True
        menu_choice = input(user_prompt).strip().lower()
        # Converts user's input to lowercase AND strips any leading/trailing space(s)
        if menu_choice.upper() == "A":
            menu_choice = menu_options[0]
            print(
                f"\nOK. {student_name}'s name will be changed in the student "
                + "database."
            )
            input("\nPress ENTER to continue >> ")
            print("\n" + "—" * 120)
        elif menu_choice.upper() == "B":
            menu_choice = menu_options[1]
            print(f"\nOK. {student_name} will now score points for an assignment.")
            input("\nPress ENTER to continue >> ")
            print("\n" + "—" * 120)
        elif menu_choice.upper() == "C":
            menu_choice = menu_options[2]
            print(
                f"\nOK. {student_name} will now score extra credit points in"
                + "\nthe gradebook."
            )
            input("\nPress ENTER to continue >> ")
            print("\n" + "—" * 120)
        elif menu_choice.upper() == "D":
            menu_choice = menu_options[3]
            print(f"\nOK. Gathering {student_name}'s updated grade status...")
        elif menu_choice.upper() == "E":
            menu_choice = menu_options[4]
            print(f"\nOK. The grading for {student_name} will now close.")
            print("\n" + "—" * 120)
            input("\nPress ENTER to exit the demo >> ")
            # End the program
        elif menu_choice in menu_options:
            if menu_choice == menu_options[0]:
                print(
                    f"\nOK. {student_name}'s name will be changed in the student "
                    + "database."
                )
                input("\nPress ENTER to continue >> ")
                print("\n" + "—" * 120)
            elif menu_choice == menu_options[1]:
                print(f"\nOK. {student_name} will now score points for an assignment.")
                input("\nPress ENTER to continue >> ")
                print("\n" + "—" * 120)
            elif menu_choice == menu_options[2]:
                print(
                    f"\nOK. {student_name} will now score extra credit points in"
                    + "\nthe gradebook."
                )
                input("\nPress ENTER to continue >> ")
                print("\n" + "—" * 120)
            elif menu_choice == menu_options[3]:
                print(f"\nOK. Gathering {student_name}'s updated grade status...")
            else:
                print(f"\nOK. The grading for {student_name} will now close.")
                print("\n" + "—" * 120)
                input("\nPress ENTER to exit the demo >> ")
                # End the program
        else:
            # A different type of value was entered
            valid_input = False
            print(
                f"\nError: '{menu_choice}' is an invalid selection. Please try "
                + "again."
            )
    return menu_choice


# Begin program execution
print(
    "—" * 120
    + "\n"
    + format(
        "Module 04 Python Programming Exercise(s): Student Grade Class Demo", "^120"
    )
    + "\n"
    + format("Week 5 Project: Part B — Student Grade Class — Grade Calculator", "^120")
    + "\n"
    + format("Written By David Wilson for Tim McMichael's Python Class", "^120")
    + "\n"
    + format(
        "Date Modified: " + format(date(2025, 10, 26).strftime("%m/%d/%Y")), "^120"
    )
    + "\n"
    + "—" * 120
)

if __name__ == "__main__":  # Checks to confirm this is the active program
    print(
        "\n"
        + format("Welcome to the StudentGrade Class Demo — Grade Calculator!", "^120")
        + "\n\n"
        + "—" * 120
    )
    input("\nPress ENTER to begin the demo >> ")
    print("\n" + "—" * 120)
    main()
    print(f"\nData for Student {student_count} was written successfully!")
    user_choice = input("\nAdd another student to the database? Y/N >> ").strip()
    while (user_choice.upper() != "Y") and (user_choice.upper() != "N"):
        print(f"\nError: '{user_choice}' is an invalid selection. Please try again.")
        print("\n" + "—" * 120)
        user_choice = input("\nAdd another student to the database? Y/N >> ").strip()
    while (user_choice == "Y") or (user_choice == "y"):
        print("\nOK. The program is reloading...")
        print("\n" + "—" * 120)
        main()
        print(f"\nData for Student {student_count} was written successfully!")
        user_choice = input("\nAdd another student to the database? Y/N >> ").strip()
        while (user_choice.upper() != "Y") and (user_choice.upper() != "N"):
            print(
                f"\nError: '{user_choice}' is an invalid selection. Please try again."
            )
            print("\n" + "—" * 120)
            user_choice = input(
                "\nAdd another student to the database? Y/N >> ".strip()
            )
    print("\nOK. The program will now close.")
    print("\n" + "—" * 120)
    input("\nPress ENTER to end the program >> ")
    sys.exit()
# End of program
