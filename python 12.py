
# using while loop

i = 0 # initialization
while (i < 10): #condition
    print(i, end=" ")
    i += 1       #update
print()

#customizing the loop as you please. In this example, we will count down by 4
i = 32  # initialization at 32
while (i >= 0):
    print(i, end=" ")    # our print statement
    i -= 4      #update
print()

# working with both for and while loops:
# both are the same below:

initialization = 3
stop_at = 10
increment = 1

# for
for i in range(initialization, stop_at, increment):
    print("for loop: ", i, end = " ")
print()

# while
while(initialization < stop_at):
    print("while loop: ", initialization, end=" ")
    initialization += increment
print()
# else with while

i = 0
while (i < 10):
    print(i, end=" ")
    i += 1
else:
    print("Else of while")

#random other example, check to see first square >

i = 0
while (i < 10):
    if i**2 > 50:
        print("First square big enough: ", i)
        break
    i += 1
else:
    print ("None are big enough")
print()
##### Flag Variable #########

# in this example below, you do a search and return the index
index = -1      # integer flag, stays -1
i = 0
while (i < 10):
    if i ** 2 > 500:
        index = i   # update the index to whichever position it has
                    # the desired value
        break
    i += 1

if index > -1:
    print("First square big enough:", i)
else:
    print("None are big enough")

print()

#### DO WHILE LOOP ############
i = 15
print(i)    # prints i at least once no matter what
i += 1
while (i < 10):
    print(i)
    i += 1

print()

### checking if a string is uppercase or lower case #########

name = "Mostafa"
if name.isupper():
    print("Upper")
elif name.islower():
    print("Lower")
else:
    print("Mixed")