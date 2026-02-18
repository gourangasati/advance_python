def rotate_left(arr, k):
    n = len(arr)
    k = k % n  
    def reverse(a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
    
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)
    return arr
arr = [1,2,3,4,5,6,7,8]
k = 3
print(rotate_left(arr,k))