"""
Mission Phoenix

Day 7

Topic : Dictionaries{}

Author : Phoenix
"""

capitals = {"Andhra Pradesh": "Amaravathi", "Tamilnadu": "Chennai", "Kanataka": "Banglore", "Telangana": "Hyderabad"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("Delhi"))

#if capitals.get("Delhi"):
#    print("Capital exists")
#else:
#    print("Capital doesn't exist")

#capitals.update({"Maharastra": "Mumbai"})
#capitals.update({"Andhra Pradesh": "Hyderabad"})
#capitals.pop("Tamilnadu")
#capitals.pop()
#capitals.clear()

"""keys = capitals.keys() #same for values
print(keys)

for keys in capitals.key():
    print(keys)"""

#items = capitals.items()
#rint(items) #it returns a dictionary object which resembles a 2D list of tuples
for key, value in capitals.items():
    print(f"{key}: {value}")
