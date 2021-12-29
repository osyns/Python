# boolean data type (true or false)

#print("Whats is your age?")
#age = int(input())
#if age > 20:
#    print("Welcome to our app!")
#elif age > 30:
#    print("Welcome to our app!")


#print("Thanks for trying our app!")

happy = True

if happy:
    print("Yay!")
else:
    print(":(")

# or operator
name = "Mostafa"
if False or print("hey"):
    print("Unite!")
    print("a lot of stuff")

# not operator
subscribed = True
email_activated = True
points = 50
if subscribed and points > 30:
    print("Welcome!")
    points -= 30
    print("points is now: ", points)

# not operator

subscribed = False
points = 20

if not subscribed and points < 30:
    print("Redirecting to subscription page")
print(not subscribed)  # negated

print("Now loops:")

###### Introduction to loops
friends = ["abby", "Jonathan", "Becky", "Ryan"]
for friend in friends:
    print(friend)

friends2 = ["abby2", "Jonathan2", "Becky2", "Ryan2"]
for those in friends2:
    print(those, end=" ")
print()

for i in range(10):
    print(i)
    print("iteration", i + 1)

for i in range(10, 20):
    print(i, end=" ")
print()

for i in range(231, 250, 2):
    print(i, end=" ")
print()

for i in range(231, 250, 4):
    print(i, end=" ")
print()

for i in range(200, -1, -1):
    print(i, end=" ")
print()












