#AI Career Eligibility Checker
while True:
    print("\n------------ AI Career Eligibility Checker -----------\n")

    age = int(input("Enter your age: "))
    experience = int(input("Enter your years of experience: "))
    skill = input("Enter your Python skill level (Beginner/Intermediate/Advanced): ")
    while True:
        current_package = float(input("Enter your current package in LPA (<= 8): "))
        if current_package <= 8:
            break
        else:
            print("Invalid input. Package should not be more than 8 LPA.")
    skill_lower = skill.lower()
    print("\n------------ Eligibility Check Results -----------\n")
    if 21 <= age <= 35 and experience >= 2 and skill_lower in ["intermediate", "advanced"]:
        print("Eligible for AI Engineer Roadmap")
    elif experience < 2:
        print("Build more projects before switching")
    elif skill_lower == "beginner":
        print("Complete Mission Phoenix Python Foundation first")
    else:
        print("Keep learning and try again in 3 months")

    #Challenge
    if current_package < 5:
        print("Target package: 9-12 LPA")
        print("Expected growth: High")
    else:
        print("Target package: 12-18 LPA")

    #Extra
    choice = input("\nWould you like to run the program again? (yes/no): ").lower()
    if choice != "yes":
        print("\nThank you for using the AI Career Eligibility Checker!")
        break