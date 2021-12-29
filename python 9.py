# breaks and #continue key words
languages = ["C++", "Java", "Python", "Javascript", "Python", "Python"]
print("What are you searching for?")
lang = input()

#for language in languages:
   # print(language)
    # if language == lang:
    # print("We found " + lang)
    # break    # javascript is never printed
   # print("End of loop iteration")


# this algorithm helps you count the instance or continue the search
# for another instance after you already found the first one
for language in languages:
    if language == lang:
        print("We found " + lang)
        continue
    print(language + "...Not what we're looking for...")
print()

appetizers = ["chips", "wings", "pretzels"]
print("Which appetizer would you like?")

my_appetizer = input()

for appetizer in appetizers:
    if my_appetizer == appetizer:   # my user input == pretzel item
        print("We found your fav appetizer: " + my_appetizer)
        continue
    print(appetizer + " Not what I want ")



# pass key word

languages2 = ["C++", "Java", "Python", "Javascript", "Python", "Python"]

print("What are you searching for?")
lang2 = input()

for languages in languages2:
    if languages == lang2:
        pass        # you can use it to fill a part later

def do_something():
    pass
class test:
    pass





