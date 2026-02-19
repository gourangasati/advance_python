def check_equal(arr1,arr2):
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else : return False
arr1 = [3,2,5]
arr2 = [ 5,1,3]
print(check_equal(arr1,arr2))