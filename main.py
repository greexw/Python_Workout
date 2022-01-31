
def bubble_sort(list_to_sort):
    n = 1
    while n != 0: #until neither element was sorted in last run of for loop
        n = 0
        for i in range(len(list_to_sort)-1):
            if list_to_sort[i] > list_to_sort[i+1]:
                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]
                n += 1
    return list_to_sort


before_sort = [7, 1, 3, 6, 15, 2, 8, 19, 4]
print("Before sort: ", before_sort)
print("After sort: ", bubble_sort(before_sort))
