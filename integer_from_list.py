# I have written a function that takes a list of integers as an input and returns the integers joined together as a larger number
# (assuming that the list of integers are all single digit)

def integer_from_list(integerList):
    orderOfMagnitude = len(integerList)-1
    finalInteger = 0
    for currentInteger in integerList:
        finalInteger += 10**orderOfMagnitude * currentInteger
        orderOfMagnitude -= 1
    return finalInteger
print(integer_from_list([8,3,1,2]))

def integer_from_list_plural(integerList):
    orderOfMagnitude = len(integerList)-1

    #checking if there are numbers with multiple digits
    for currentInteger in integerList:
        if currentInteger / 10 >= 1:
            pass
    finalInteger = 0
    for currentInteger in integerList:
        finalInteger += 10**orderOfMagnitude * currentInteger
        orderOfMagnitude -= 1
    return finalInteger
print(integer_from_list([8,3,1,2]))
