# Takes input converts to int
# uses while loop until condition is reached

name = input("Please enter a number: ")
print("Number input was: ", name)

counter = int(name)

while counter < 20:
    counter += 2
    print (counter)
