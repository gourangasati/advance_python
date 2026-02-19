def equli(arr):
    total = sum(arr)
    left = 0
    for i in range(len(arr)):
        right = total - left - arr[i]
        if left == right :
            return i
        left += arr[i]
arr = [1,3,5,2,2]
print(equli(arr))