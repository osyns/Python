import math
age = 15
age_str = str(age)
id_age_str = id(age_str)
other = math.floor(2.6)
added = id_age_str + other
added_str = str(added)
length = len(added_str)
#print(length)

# nesting is a lot cleaner
#print(len(str(id(str(age)) + math.floor(2.6))))

# LISTS:
ages = [12, 18, 28]
people = ["Caleb", "Sabrina", "emily"]
my_favorite_things = ["working out", 7, ['amazon prime', 'netflix']]

print(id(my_favorite_things))
my_favorite_things[0] = "walking"
print(id(my_favorite_things))

# lists are mutable


my_favorite_things1 = ["working out", 7, ['amazon prime', 'netflix']]
copy = my_favorite_things1.copy()
print(copy)
copy[0] = "walking"

print(my_favorite_things1, copy)





