def max_difference(arr):
    if len(arr) < 2:
        return 0
    
    min_so_far = arr[0]
    max_diff = arr[1] - arr[0]
    
    for j in range(1, len(arr)):
        max_diff = max(max_diff, arr[j] - min_so_far)
        min_so_far = min(min_so_far, arr[j])
        
    return max_diff

arr = [1,4,2,5,6]
print(max_difference(arr))
