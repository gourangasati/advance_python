def subarray(arr,val):
    i = 0
    curr = 0
    for j in range(len(arr)):
        curr += arr[j]
        while curr > val:
            curr -= arr[i]
            i+= 1
        if curr == val:
            return arr[i:j+1]
    return None
arr = [1,2,3,4,3,4,1]
tar = 11
print(subarray(arr,tar))