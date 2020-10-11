import random
from heapq import heapify,heappush,heappop

li = list(range(10000))
random.shuffle(li)



def topk(li,k):
    heapify(li)

    topk = []
    n = 1

    while n<=k:
        item = heappop(li)
        topk.append(item)
        n = n+1
    return topk

print(topk(li,10))
