"""
T1 - 5
T2 - 4
T3 - 7
T4 - 9
T5 - 2
T6 - 6
"""

import heapq

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]

# print(sorted(data))
heapq.heapify(data)
print(data)

copy = data[:]
popped_val = heapq.heappop(data)
print(popped_val)
print(copy.pop(0))

print(data)

heapq.heapify(copy)
print(copy)

heapq.heappush(data, 4)
heapq.heappush(data, 19)
heapq.heappush(data, 21)

print(data)

# How to convert the min heap to max heap
# data = [-x for x in data]

heapq._heapify_max(data)
print(data)
max_val = heapq._heappop_max(data)
print(max_val)

l1 = [10, 20, 30, 40, 50]
l2 = [15, 25, 35, 45, 55]
l3 = heapq.merge(l1, l2)
print(l3)

"""
i
2*i+1
2*i+2

"""