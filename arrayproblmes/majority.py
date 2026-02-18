def majority(arr):
    count = 0
    candidate = None
    for val in arr:
        if count == 0:
            candidate = val
        count += 1 if val == candidate else -1
    return candidate
arr = [1,2,3,2,6,2,2]
print(majority(arr))