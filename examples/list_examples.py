# List Example

my_shopping_list = ["bread", "oranges", "newspaper"]

# print type
print (type(my_shopping_list))

# print list
print (my_shopping_list)

# print item from list
print ("The item is: " , my_shopping_list[1])

# looping over a list
for item in my_shopping_list:
    print (item)

# looping over a list with a conditional
for item in my_shopping_list:
    if item == "oranges":
        print ("I found the item ", item)

# append item to end of list
my_shopping_list.append("apples")
print (my_shopping_list)


