def subarray(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            result.append(arr[i:j+1])
    return result
arr = [1,2,3,4,5,6]
print(subarray(arr))