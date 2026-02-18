def remove(arr,tar):
    result = []
    for val in arr:
        if val != tar:
            result.append(val)
    return result
arr = [1,3,2,5,7]
element = 5
print(remove(arr,element))