def find_pair(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return complement, num
        seen.add(num)
    return None
arr = [2,4,5,7,9]
tagret = 6
print(find_pair(arr,tagret))