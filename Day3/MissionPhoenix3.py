"""
Mission Phoenix

Day 3

Topic : Input

Author : Phoenix
"""

"""
project_name = input("Enter the project name: ")
days_remaining = int(input("Enter the number of days remaining: "))
days_remaining = days_remaining - 1
print(f"Project Name: {project_name}")
print(f"Days Remaining: {days_remaining}")
"""
"""
#Assignment mad libs
project_name = input("Enter the project name: ")
days_remaining = input("Enter the number of days remaining: ")
day_of_project = input("Enter the day of the project: ")
package = input("Enter the package offered: ")
programming_language = input("Enter the programming language you are using: ")

print(f"I started working on the project {project_name} from monday")
print(f"The project is due in {days_remaining} days")
print(f"Today is the day {day_of_project} of the project")
print(f"The mission of this project is to complete it successfully and crack a new job with {package} LPA")
print(f"The progress I'm making on {programming_language} is great")
"""

#Assignment area calculator of circle
"""
radius = float(input("Enter the radius of the circle: "))
pie = float(input("Enter the value of pie: "))

area = pie * radius * radius
print(f"The area of the circle with radius {radius} is: {area}cm^2")
"""
#Salary Growth Calculator
current_salary = float(input("Enter your current salary: "))
target_salary = float(input("Enter your target salary: "))
salary_increase = target_salary - current_salary
percentage_increase = (salary_increase / current_salary) * 100

print(f"Your current salary is: {current_salary}")
print(f"Your target salary is: {target_salary}")
print(f"You need a salary increase of: {salary_increase}")
print(f"This is a percentage increase of: {round(percentage_increase, 2)}%")

if salary_increase < 0:
    print("Your target salary is lower than your current salary.")
else:
    print("Congratulations! You are aiming for a higher salary.")
    