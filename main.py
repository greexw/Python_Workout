#Convert number to reversed array of digits
#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

#Example:
#348597 => [7,9,5,8,4,3]
#0 => [0]

def convert(number):
    string = str(number)
    array = []
    for c in reversed(string):
        array.append(int(c))
    return array


print(convert(348597))
