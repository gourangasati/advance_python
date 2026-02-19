arr = [1,2,3,4,5,6,7,8,9,10]
k  = 3
arr = arr[::-1]
arr = arr[:3][::-1] + arr[3:][::-1]
print(arr)
