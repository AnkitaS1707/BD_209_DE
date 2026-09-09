"""
Student Grades Manager
------------------------
Stores student names and grades in a dictionary.
Lets the user add a new student, update an existing grade,
or print all grades, using basic dictionary operations and if/else.
"""

# Dictionary to hold student names (keys) and grades (values)
student_grades = {}


def add_student():
    name = input("Enter student name: ").strip()
    grade = input(f"Enter grade for {name}: ").strip()

    if name in student_grades:
        print(f"'{name}' already exists with grade {student_grades[name]}.")
        print("Use option 2 if you want to update their grade instead.")
    else:
        student_grades[name] = grade
        print(f"Added '{name}' with grade {grade}.")


def update_grade():
    name = input("Enter student name to update: ").strip()

    if name in student_grades:
        new_grade = input(f"Enter new grade for {name}: ").strip()
        old_grade = student_grades[name]
        student_grades[name] = new_grade
        print(f"Updated '{name}': {old_grade} -> {new_grade}")
    else:
        print(f"'{name}' not found. Use option 1 to add them first.")


def print_grades():
    if not student_grades:
        print("No students in the record yet.")
    else:
        print("\n--- Student Grades ---")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
        print("-----------------------")


def show_menu():
    print("\nWhat would you like to do?")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            update_grade()
        elif choice == "3":
            print_grades()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()