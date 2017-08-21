list1 = [1, 2, 1,6, 3, 4, 5, 9]


def binary_search_impl(arr, start, end, key):

    if start <= end:
        mid = start + (end-start)/2
        if arr[mid]==key:
            return mid
        elif arr[mid] > key:
            return binary_search_impl(arr, start, mid-1, key)
        else:
            return binary_search_impl(arr, mid+1, end, key)
    else:
        return -1


def binary_search(arr, key):
    if arr is None or key is None:
        return -1
    else:
        start = 0
        end = len(arr)-1
        arr.sort()
        print arr
        return binary_search_impl(arr, start, end, key)


print binary_search(list1, 2)

