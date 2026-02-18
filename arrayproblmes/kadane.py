def maxsub(arr):
    curr  = maxs  =  arr[0] 
    for i in range(1,len(arr)):
        curr = max(curr+arr[i], curr)
        maxs = max(maxs,curr)
    return maxs
arr = [1,2,3,4,7,8,-4]
print(maxsub(arr))