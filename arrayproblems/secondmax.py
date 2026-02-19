arr = [21,43,54,65,76,87,98,12,34,56]
largest = second_largest = float('-inf')
for num in arr:
    if num> largest:
        second_largest = largest
        largest = num
    elif num> second_largest and num < largest:
        second_largest = num
print("Second largest element is:", second_largest)