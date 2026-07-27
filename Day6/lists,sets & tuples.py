"""
Mission Phoenix

Day 6

Topic : Lists, sets & tuples

Author : Phoenix
"""
"""
#Lists

teams = ["omni", "MP S&S", "US RD", "EU RD"]
print(teams)
#print(teams[0])
#print(teams[:2])
#print(teams[::2])
#print(dir(teams))
#print(help(teams))
#print(len(fruits))
#print("LAC" in teams)

#teams[0] = "LAC"
#teams.append("LAC")
#teams.remove("EU RD")
#teams.insert(1, "LAC")
#teams.sort()
#teams.reverse()
#teams.clear()
#print(teams.index("omni"))

for team in teams:
    print(team)

#Set

teams = {"omni", "MP S&S", "US RD", "EU RD", "EU RD"}
print(teams)
#print(dir(teams))
#print(help(teams))
#print(len(fruits))
#print("LAC" in teams)
#print(teams[0]) - typeError
#teams.add("LAC")
#teams.remove("EU RD")
#teams.pop() - removes 1st element[random everytime]

#Tuples

teams = ("omni", "MP S&S", "US RD", "EU RD", "US RD")
print(teams)
#print(dir(teams))
#print(help(teams))
#print(len(fruits))
#print("LAC" in teams)

#print(teams.index("omni"))
#print(teams.count("US RD"))

for team in teams:
    print(team)
"""

#Practice

teams = []
zones = []
no_of_team = 0

while True:
    team = input("Enter your team name(q to quit): ")
    if team.lower() == "q":
        break
    else:
        zone = int(input("Enter zone number: "))
        teams.append(team)
        zones.append(zone)
    
print("=====FLOOR MAP=====")

print(f"{teams}, \n{zones}")