def merge(arr1,arr2):
    i = j = 0
    n = len(arr1)-1
    m = len(arr2)-1
    result = []
    while i<= n and j <=m:
        if arr1[i]> arr2[j]:
            result.append(arr2[j])
            j+= 1
        else:
            result.append(arr1[i])
            i+= 1
    while i <= n :
        result.append(arr1[i])
        i+= 1
    while j<=m :
        result.append(arr2[j])
        j+= 1
    return result

arr1 =  [1,3,4,5,6]
arr2 = [2,3,4,5,8]
print(merge(arr1,arr2))