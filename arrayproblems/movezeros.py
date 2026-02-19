def move_zeros(arr):
    j = 0
    n = len(arr)-1
    for i in range(n):
        if arr[i] == 0:
            j = i 
            break
    for i in range(j+1,n):
        if arr[i]!= 0:
            arr[j],arr[i] = arr[i],arr[j]
            j += 1
arr=[1,0,4,3,2,5,0,9,8,4,0]
move_zeros(arr)
print(arr)