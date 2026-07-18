#project on basics
"""
Mission Phoenix

Day 3

Topic : Input

Author : Phoenix
"""
while True:
    name = input("Enter Employee name: ")
    current_salary = float(input("Enter your current salary (LPA): "))
    experience = int(input("Enter your experience (in years): "))
    performance_rating = float(input("Enter performance rating (1-5): "))

    if experience >= 5 and performance_rating >= 4.5:
        salary_hike = 30
        print("Promotion Eligible\nSalary Hike: 30%")
    elif experience >= 3 and performance_rating >= 4:
        salary_hike = 20
        print("Salary Hike: 20%")
    elif performance_rating < 3:
        salary_hike = 0
        print("Performance Improvement Plan Required")
    else:
        salary_hike = 10
        print("Salary Hike: 10%")

    new_salary = current_salary + (current_salary * salary_hike / 100)
    print("\n=========================\n")
    print(f"Current Salary: {current_salary:.2f}\nHike: {salary_hike}%\nNew salary: {new_salary:.2f} LPA")
    print("\n==========================================\n")
    print("          Employee Evaluation report          ")
    print("\n==========================================\n")
    print(f"Employee Name      : {name}")
    print(f"Experience         : {experience}")
    print(f"Performance Rating : {performance_rating}")
    print(f"Current Salary     : {current_salary}")
    print(f"Salary Hike        : {salary_hike}")
    print(f"New Salary         : {new_salary}")
    print(f"Decision           : {'Salary Hike Approved' if new_salary > current_salary else 'No Salary Hike'}")
    print("\n==========================================\n")
    while True:
        evaluate = input("\n Evaluate another employee? (yes/no): ").lower()
        if evaluate != "yes":
            print("\nThank you")
            break
    break
  