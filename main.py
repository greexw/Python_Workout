#Find the stray number
# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
#
# Complete the method which accepts such an array, and returns that single different number.
#
# The input array will always be valid! (odd-length >= 3)
#
# Examples
# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3


def stray(arr):
    x_count, y_count = 0, 0
    x, y = arr[0], None
    for number in arr:
        if number == x:
            x = number
            x_count += 1
        else:
            y = number
            y_count += 1

    if x_count == 1:
        return x
    elif y_count == 1:
        return y
    else:
        return "error"


print(stray([2, 3, 2, 2, 2]))
print(stray([1, 1, 1, 1, 1, 1, 2]))
print(stray([3, 2, 2, 2, 2]))
