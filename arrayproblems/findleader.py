def find_leader(arr):
    idx = 0
    for i in range(1,len(arr)-1):
        if arr[i]>arr[idx]:
            idx = i
    return arr[idx]
arr = [3,2,4,3,4,2]
print(find_leader(arr))