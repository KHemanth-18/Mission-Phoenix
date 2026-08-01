"""
Mission Phoenix

Day 7

Topic : Student Management System

Author : Phoenix
"""

students = []
#Add Student
def add_student():
    name = input("Enter Student name:").strip()
    if name == "":
        print("Student name can't be empty.")
        return
    age_input = input("Enter age: ")
    if not age_input.isdigit():
        print("Age must be number.")
        return
    age = int(age_input)
    grade = input("Enter grade: ").strip()
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print(f"{name} added successfully")

#View Students
def view_students():
    if len(students) == 0:
        print("No students found.")
        return
    
    print("\nStudent List: ")
    for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

#Update Student
def update_student():
    name = input("Enter name to update: ").strip()
    for student in students:
        if student["name"].lower() == name.lower():
            new_age_input = input("Enter new age: ")
            if not new_age_input.isdigit():
                print("Age must be number.")
                return
            new_age = int(new_age_input)
            new_grade = input("Enter new grade: ").strip()
            student["age"] = new_age
            student["grade"] = new_grade
            print(f"{name} updated successfully.")
            return
    print("Student not found.")

#Search Student
def search_student():
    name = input("Enter name to search: ").strip()
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Found → Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            return
    print("Student not found.")

#Remove Student
def remove_student():
    if len(students) == 0:
        print("No students found.")
        return
    
    name = input("Enter name to remove: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Removing student: Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            confirmation = input("Are you sure (Y/N): ").strip().lower()
            if confirmation != "y":
                print("Removal cancelled.")
                return
            else:
                students.remove(student)
                print("Student removed successfully.")
            return

    print("Student not found")

#count Students
def count_students():
    print(f"Total Students: {len(students)}")

while True:
    print("\n========== Student Management ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Remove Student")
    print("6. Count Students")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        search_student()
    elif choice == "5":
        remove_student()
    elif choice == "6":
        count_students()
    elif choice == "7":
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.")  