# Student Management System

file_name = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")

    with open(file_name, "a") as f:
        f.write(f"{roll},{name},{course}\n")

    print("Student added successfully!\n")


def view_students():
    try:
        with open(file_name, "r") as f:
            data = f.readlines()

            if not data:
                print("No students found.\n")
                return

            print("\n--- Student List ---")
            for line in data:
                roll, name, course = line.strip().split(",")
                print("Roll:", roll, "| Name:", name, "| Course:", course)

    except FileNotFoundError:
        print("No data file found.\n")


def search_student():
    roll_search = input("Enter roll number to search: ")

    with open(file_name, "r") as f:
        for line in f:
            roll, name, course = line.strip().split(",")

            if roll == roll_search:
                print("Student Found!")
                print("Name:", name)
                print("Course:", course)
                return

    print("Student not found.\n")


def delete_student():
    roll_delete = input("Enter roll number to delete: ")

    lines = []
    found = False

    with open(file_name, "r") as f:
        lines = f.readlines()

    with open(file_name, "w") as f:
        for line in lines:
            roll, name, course = line.strip().split(",")

            if roll != roll_delete:
                f.write(line)
            else:
                found = True

    if found:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


while True:
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice!")
