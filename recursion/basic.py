def allpur(arr):
    n = len(arr)
    hmap = {}
    res = []
    def calpur(ds):
        if len(ds) == n:
            res.append(ds.copy())
            return 
        for j in range(n):
            if j not in hmap or not hmap[j]:
                hmap[j] = True
                ds.append(arr[j])
                calpur(ds)
                ds.pop()
                hmap[j] = False
    calpur([])
    return res
print(allpur([1,2,3]))
