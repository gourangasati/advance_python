def first_missing_positive(arr):
    arr = sorted(arr)
    smallest = 1
    
    for num in arr:
        if num == smallest:
            smallest += 1
            
    return smallest
arr = [-3,-4,-2,0,3,2,1,8,7,6,5]
print(first_missing_positive(arr))