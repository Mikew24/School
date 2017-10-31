import heapq
#heap
k=heapq
d=[5,4,32,1,4,6,7,87]
k=[5,4,32,1,4,6,7,87]
s=[]
heapq.heapify(d)
for aa in range(len(d)):
    s.append(heapq.heappop(d))
print(s)
