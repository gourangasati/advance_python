def finddup(arr):
    seen = set()
    for val in arr:
        if val in seen:
            return True
        seen.add(val)
    return False
arr = [1,2,3,4,5]
print(finddup(arr))