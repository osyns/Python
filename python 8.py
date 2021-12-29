# using range
# sum of numbers within range below:

for i in range(10):
    print(i)
print(sum(range(10)))

# algorithmic way:
sum = 0
for i in range(10):
    print(i)
    sum += 1  # for each iteration in this loop, we will add sum
print(sum)     # printing sum

for i in range(10):
    print(i, end=" ")
print()

my_list = range(10)     # when we invoke range doesn't give you a list back
print(my_list)          # output will be range(0,10)
                        # we need to get this below:
my_list = list(range(10))     # my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list)                # print(my_list)



foods = ["asparagus", "tacos", "strawberries", "yogurt", "bagels"]
for i in range(10):
    print(i, end=" ")
print()

for food in foods:
    print(food, end=" ")
print()

for i in range(len(foods)):
    print(i, foods[i], end=" ")
print()

print(len(foods))

languages = ["C++", "Java", "Python"]
for i in range(len(languages)):
    print(i, languages[i], end=" ")