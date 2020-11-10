# creating and printing a dictionary
my_dictionary = {"colour": "black",
                 "brand": "New Balance",
                 "model": 373, }
print (my_dictionary)

# print keys in dictionary
for item in my_dictionary:
    print (item)

# print values in dictionary
for item in my_dictionary:
    print (my_dictionary[item])

# print keys and values in dictionary
for key,value in my_dictionary.items():
    print (key,value)

# check for a key in dictionary
if 'colour' in my_dictionary:
    print ("The key is in the dictionary")
