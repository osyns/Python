# flags
'''''''''
numbers = [5, 3, 6, 70, 4, 2, 4, 3]
i = 0
square = 500
success = False    # flag

while i < len(numbers):
    if numbers[i] ** 2 > square:
        print(numbers[i], "square is larger than", square)
        success = True   # change the flag
        break
    print(numbers[i], "squared is not larger than", square)
    i += 1
if success:             # use this instead of else statement
    print("one of them was large enough")

print()
'''''''''

'''''''''
 do while loop:
    i = 90
    print(i)
    i += 1
print()

i = 0
while i < 10:
    print(i)
    i += 1

i = 0
while True:
    print(i)
    i += 1
    if i > 9:
        break
'''''''''
# creating an indefinite loop
# an example of asking the use whether they want to continue or no
'''''''''
print("Do you want to continue? Y/N")
response = input()
while response == "Y":
    print("Do you want to continue? Y/N")
    response = input()
'''''''''
'''''''''
while True:
    print("Q to quit. Continuing ...")
    response = input()
    if response == "Q":
        break
'''''''''

# casing and characters:
'''''''''
 while True:
    print("Continue? Y/N")
    response = input()
    if response == 'Y'or response == 'y':    # demorgan's law
        continue
    break
'''''''''
'''''''''
while True:
    print("Continue? Y/N")
    response = input()
    if response.lower() != 'y':   # the lower method
        break
'''''''''
'''''''''
while True:
    print("Continue? Y/N")
    response = input()
    if response.upper() != 'Y': # The upper method
        break
# these methods for string comparison for lowering or upper casing a string
# strings have methods such as lower and upper
'''''''''''

# special case to test whether a string is lower case or upper case
while True:
    print("Continue? Y/N")
    response = input()
    if response.isupper():
        print("It's upper")
    if response.lower() != 'y':
        break