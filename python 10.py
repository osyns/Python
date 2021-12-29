# else statement


# both options below:

languages = ["C++", "Java", "Python", "JavaScript", "Python", "Python"]

print("What are you searching for? ")
lang = input()

found = False   # boolean

for language in languages:
    if language == lang:
        print(language + " was found.")
        found = True
        break
if not found:
    print("Not found")


languages = ["C++", "Java", "Python", "JavaScript", "Python", "Python"]

print("What are you searching for? ")
lang = input()

for language in languages:
    if language == lang:
        print(language + "was found")
else:
    print("loop is done")


i = 0                 # First the initialization
while i <= 10:        # This is called the condition, same as range(10)
    print(i)          #
    i += 2            # update how to get from one to the other
print()

i = 0                      # always need to initialize
while i < 10:
    print(i)
    i += 1
print()

# the for loop
for i in range(10): # same as for i in range(0,10,1)
    print(i)
print()
print()

numbers = [5, 3, 6, 7, 4, 2, 4, 3]
i = 0
square = 500
while i < len(numbers):   # i < the length of numbers
    if numbers[i] ** 2 > square:
        print(numbers[i], "squared is larger than", square)
        break         # using the very first number in list that is larger than 500
    print(numbers[i], "squared is not larger than", square)
    i += 1
else:
    print("None squared are larger than", square)
