"""
Mission Phoenix

Day 7

Topic : Employee Management System

Author : Phoenix
"""
employees=[]
#Add employee
def add_employee():  
    name = input("Enter the employee name: ").strip()
    if name == "":
        print("Employee name can't be empty.")
        return
    age_input = input("Enter age: ")
    if not age_input.isdigit():
        print("Age must be number.")
        return
    age = int(age_input)
    department = input("Enter department: ").strip()
    employee = {"name": name, "age": age, "department": department}
    employees.append(employee)
    print(f"{name} added successfully")        

#View employees
def view_employees():
    if len(employees) == 0:
        print("No employees found.")
        return
    
    print("\nEmployee List: ")
    for employee in employees:
            print(f"Name: {employee['name']}, Age: {employee['age']}, Dept: {employee['department']}")

#Search employee
def search_employee():
    name = input("Enter name to search: ").strip()
    for employee in employees:
        if employee["name"].lower() ==name.lower():
            print(f"Found → Name: {emp['name']}, Age: {emp['age']}, Dept: {emp['department']}")
            return
    print("Employee not found.")


#Remove employee
def remove_employee():
    name = input("Enter name to remove: ").strip()

    for emp in employees:
        if emp["name"].lower() == name.lower():
            employees.remove(emp)
            print("Employee removed successfully.")
            return

    print("Employee not found")
    
#Count employees
def count_employees():
    print(f"Total employees: {len(employees)}")

while True:
    print("\n========== Employee Management ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Count Employees")
    print("6. Add Employee")
    print("=========================================")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        remove_employee()
    elif choice == "5":
        count_employees()
    elif choice == "6":
        print("Exit")
        break
    else:
        print("Invalid choice. Please enter 1-6: ")