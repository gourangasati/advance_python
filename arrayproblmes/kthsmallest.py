import heapq
def kthsmallest(arr,k):
    heap = []
    for val in arr:
        heapq.heappush(heap,val)
    for i in range(k-1):
        heapq.heappop(heap)
    return heapq.heappop(heap)
arr = [1,2,3,4,5,6,7,8]
k = 3
print(kthsmallest(arr,k))