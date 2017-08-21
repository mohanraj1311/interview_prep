from heapq import *
import heapq


def kth_largest_elem(num, k):
    if k > len(num):
        return None

    heap_array = []

    for i in xrange(len(num)):
        heapq.heappush(heap_array, num[i])

        if len(heap_array)>k:
            heapq.heappop(heap_array)

    return heap_array[0]

num = [18, 12, 3, 4, 1, 5, 6, 10]

kth_largest = kth_largest_elem(num, 3)
print kth_largest
heapify(num)
print num
#assert kth_largest == num[3]







