#Job Offer Decision System

offered_package = float(input("Enter the offered package (LPA): "))
work_mode = input("Enter work mode (Remote/Onsite/Hybrid): ")
bond = int(input("Enter bond period (in years): "))
rating = float(input("Enter company rating (1-5): "))

if offered_package >= 9 and rating >= 4 and bond <= 1:
    print("Excellent opportunity! Accept the offer.")
elif offered_package < 9:
    print("Negotiate for a better package")
elif bond > 2:
    print("Think carefully before accepting a long bond.")
elif rating < 3:
    print("Research the company before making a decision.")
else:
    print("This offer is decent. Compare it with other opportunities.")

#Bonus Challenge

if work_mode.lower() == "remote":
    print("Work-life balance advantage detected.")
elif work_mode.lower() == "hybrid":
    print("Balanced work environment.")
elif work_mode.lower() == "onsite":
    print("Daily commute required.")
else:
    print("Invalid work mode entered.")

print("\n============ Job offer summary ============")
print(f"Offered Package: {offered_package} LPA")
print(f"Work Mode: {work_mode}")
print(f"Bond Period: {bond} years")
print(f"Company Rating: {rating}/5")
print(f"Decision: {'Excellent opportunity!' if offered_package >= 9 and rating >= 4 and bond <= 1 else 'Negotiate/Research/Think carefully based on the conditions.'}")
print("===========================================")