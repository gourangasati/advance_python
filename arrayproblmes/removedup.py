def remove_dup(arr):
    seen = set()
    for i in range(len(arr)-1):
        if arr[i] in seen:
            arr.pop(i)
        seen.add(arr[i])
arr = [1,1,2,3,4,5,6]
remove_dup(arr)
print(arr)