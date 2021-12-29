#indexes and string slicing

poem = "Where am I?"
print(poem[2:]) #inclusive
print(poem[:2]) #exclusive
print(poem[5:])  #notice inclusive
print(poem[-5:]) # we are now starting from the right
print(poem[:7])
print(poem[-7])  #starting -1 from the right
print(poem[:-7])

# more on slicing
print(poem[6:8])            #same thing
print(poem[6:-3])           #same thing

start = 6
print(poem[start:start+2])   #same thing

name = "Mostafa YERR"
start_of_last = 6
print(name[start_of_last:start_of_last+3])