import copy

# this is how you do deepcopy in python
my_favorite_things = ["Working out", 7, ['amazon prime', ['netflix', 'hulu']]]
c = copy.deepcopy(my_favorite_things)
print(len(my_favorite_things[2][1]))
# copying lists
copy = my_favorite_things.copy()

print(my_favorite_things, copy)

print(id(c[2]))
print(id(my_favorite_things[2]))
copy[2][0] = "Hulu"

print(my_favorite_things, c)




my_favorite_things_1 = ["working out", 7, ["amazon prime","netflix"]]
least_favorite_1 = ["onions", "javaScript"]
print(my_favorite_things_1 + least_favorite_1)

least_favorite_1.append("editing")

print(least_favorite_1)
print(my_favorite_things_1 + least_favorite_1)
