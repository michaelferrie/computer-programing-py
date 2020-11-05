count = 0
vowels = 'aeiou'
value = input("Please enter a string: ")
print('You entered: ' + (value))

for item in value:
    if item in vowels:
        print (item)
