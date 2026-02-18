def find_miss(arr,n):
    arr.sort()
    if arr[0] != 1:
        return 1
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i] > 1 :
            return arr[i]+1
    return n
arr= [3,1,7,6,4,2,8,5]
n = 9
print(find_miss(arr,n))