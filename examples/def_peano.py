# Peano Addition

def peano_addition(first_number, second_number):
    if first_number == 0:
        print ("The sum of the two numbers is: ", second_number)
    while first_number >= 1:
        first_number -= 1
        second_number += 1
        print ("The first number is now: ", first_number)
        print ("The second number is now: ", second_number)
        #return (second_number)

print (peano_addition(126354685,135465465))
