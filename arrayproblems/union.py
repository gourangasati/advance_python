def union(arr1, arr2):
    return list(set(arr1) | set(arr2))
arr1 = [2,5]
arr2 = [3,6]
print(union(arr1,arr2))