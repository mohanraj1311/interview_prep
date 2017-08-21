import heapq


min_heap = []
max_heap = []


def add_num(num):
    if len(min_heap) == 0 and len(max_heap) == 0:
        heapq.heappush(min_heap, num)

    elif len(min_heap) > len(max_heap):
        if num > min_heap[0]:
            heapq.heappush(max_heap, -1*heapq.heappop(min_heap))
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -1*num)

    elif len(max_heap) > len(min_heap):
        if num < -1*max_heap[0]:
            heapq.heappush(min_heap, -1*heapq.heappop(max_heap))
            heapq.heappush(max_heap, -1*num)
        else:
            heapq.heappush(min_heap, num)

    else:
        if num > min_heap[0]:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -1*num)

    return


def find_median(arr1, arr2):
    for each in arr1:
        add_num(each)
    for each in arr2:
        add_num(each)

    if len(min_heap) > len(max_heap):
        return min_heap[0]
    elif len(max_heap) > len(min_heap):
        return -1*max_heap[0]

    else:
        return float(-1*max_heap[0] + min_heap[0])/2


num1 = [1,2]
num2 = [3,4]

print find_median(num1, num2)
