programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "The action of doing something over and over again", }

# Adding new items to dictionary
programming_dictionary["Binary"] = "A way of representing information using only two options."


print(programming_dictionary["Loop"])
print(programming_dictionary)

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
