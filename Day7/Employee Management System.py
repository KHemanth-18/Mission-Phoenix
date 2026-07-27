"""
Mission Phoenix

Day 7

Topic : Dictionaries{}

Author : Phoenix
"""
employees=[]
#Add employee
def add_employee():  
    employee_name = input("Enter the employee name: ").strip()
    if employee_name == "":
        print("Employee name can't be empty.")
        return
    employees.append(employee_name)
    print(f"{employee_name} added successfully")        

#View employees
def view_employees():
    if len(employees) == 0:
        print("No employees found.")
    else:
        print("\nEmployee List: ")
        for employee in employees:
            print("-", employee)

#Search employee
def search_employee():
    employee_name = input("Enter name to search: ").strip()
    if employee_name in employees:
        print(f"{employee_name} found.")
    else:
        print(f"{employee_name} not found.")

#Remove employee
def remove_employee():
    employee_name = input("Enter name to remove: ").strip()
    if employee_name in employees:
        employees.remove(employee_name)
        print(f"{employee_name} removed successfully.")
    else:
        print(f"{employee_name} not found.")

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
    if choice == "2":
        view_employees()
    if choice == "3":
        search_employee()
    if choice == "4":
        remove_employee()
    if choice == "5":
        count_employees()
    if choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1-6: ")