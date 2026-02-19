arr = [1,1,1,2,3,4,2,2,1,2,3,4,5,6,7,8,9,10]
dict = {}
for val in arr:
    dict[val] = dict.get(val, 0) + 1
print(dict)