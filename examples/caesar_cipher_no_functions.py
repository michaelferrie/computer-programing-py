# Michael Ferrie
# Crack a Caesar Cipher without functions
# 7/10/2020

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = 1
cipher = 'dbu'
starter_key_list = []
final_key_list = []

# get an index position for every letter in cipher
for item in cipher:
    if item in letters:
        index = letters.index(item)
        starter_key_list.append(index)
#print (starter_key_list)
        
# modify index to new position using key and pass to new list
for item in starter_key_list:
    item -= key
    item = (item % 26)
    final_key_list.append(item)
#print (final_key_list)

# match the new index to the letter index
for found in final_key_list:
    for (index, item) in enumerate(letters):
        if index == found:
            print (item)
