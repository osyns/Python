# the immutability of strings
# once a string is created we can't change that string
# strings can't be changed
# numbers are immutable as well and other objects

task = "Subscribe"
print(id(task))

task = task + "!"
print(id(task))

# However, there are objects that support change
# That is lists

# we will know learn important string function in python
msg = "please subscribe"
print(msg)
print(len(msg))
print(msg[15])          #the max index are the (total length - 1)
print(msg[len(msg)-1])  #the last character at 15 is e

print(msg[14])


# How to convert a number to a string

msg = "please subscribe"
# note that up here we had to convert the number to a string
# because you can't concatenate a string and an integer
print("Your message was " + str(len(msg)) + " characters long")

# we get the same output with no conversions and concatenations
# this option is not always available when we are working with other functions with data in it but with print it works
print("Your message was", len(msg), "characters long")