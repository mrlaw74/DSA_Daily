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
            temp = my_arr[j+1]
            my_arr[j] = my_arr[j+1]
            my_arr[j+1] = temp
            # my_arr[j], my_arr[j+1] = my_arr[j+1], my_arr[j]

print(my_arr)