def intersection(arr1,arr2):
    seen = set(arr1)
    result = []
    for val in arr2:
        if val in seen:
            result.append(val)
    return result
arr1 = [1,2,3,4,5,6]
arr2 = [6,7,8,9,0,5]
print(intersection(arr1,arr2))