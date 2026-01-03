my_array = [7, 12, 9, 4, 11]

lowest_value = my_array[0]
for val in my_array:
    if val < lowest_value:
        lowest_value = val
print(lowest_value)

# DSA Bubble Sort

# How it works:

# Go through the array, one value at a time.
# For each value, compare the value with the next value.
# If the value is higher than the next one, swap the values so that the highest value comes last.
# Go through the array as many times as there are values in the array.

my_arr = [7, 12, 9, 11, 3]

n = len(my_arr)
for i in range(n-1):
    for j in range(n-i-1):
        if my_arr[j] > my_arr[j+1]:
            my_arr[j], my_arr[j+1] = my_arr[j+1], my_arr[j]

print(my_arr)

arr = [1, 4, 2, 9, 3, 7]

n = len(arr)

for i in range (n-1):
    sorted = False
    for j in range (n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            sorted = True
    if sorted == False:
            break
print(arr)


# Selection Sort Implementation
# To implement the Selection Sort algorithm in a programming language, we need:

# An array with values to sort.
# An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. This loop must loop through one less value each time it runs.
# An outer loop that controls how many times the inner loop must run. For an array with 
# n
#  values, this outer loop must run 
# n
# −
# 1
#  times.

my_array = [64, 34, 25, 5, 22, 11, 90, 120]

n = len(my_array)

for i in range (n):
    min_val = my_array[i]
    for j in range (i+1, n):
        if my_array[j] < min_val:
            min_val = my_array[j]
    # print(min_val)
    my_array.remove(min_val)
    my_array.insert(i, min_val)

print(my_array)

# Burble sort
arr = [2,4,5,6,7,3,9,1]

n = len(arr)
for i in range(n-1):
    issorted = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            issorted = True
    if issorted == False:
        break
print(arr)


# Selection sort
arr = [3,5,7,9,2,4,6,8]

n = len(arr)
for i in range(n):
    cur_val = arr[i]
    for j in range (i+1, n):
        if arr[j] < cur_val:
            arr[j], arr[i] = arr[i], arr[j]
print(arr)

