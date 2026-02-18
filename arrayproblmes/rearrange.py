def rearrange(arr):
    arr.sort()
    n = len(arr)
    left, right = 0, n - 1
    result = []
    
    while left <= right:
        if left != right:
            result.append(arr[right])
            result.append(arr[left])
        else:
            result.append(arr[left])
        left += 1
        right -= 1
        
    return result
arr = [3,2,5,2,2,4,45,1]
print(rearrange(arr))