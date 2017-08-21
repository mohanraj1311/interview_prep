import sys


def maxsum(arr):
    if arr is None:
        return 0

    running_sum = 0
    global_sum = -sys.maxint-1

    for i in xrange(len(arr)):

        running_sum = running_sum + arr[i]
        global_sum = max(global_sum, running_sum)
        running_sum = max(0, running_sum)

    return global_sum


def main():
    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    arr1 = [-2, -3, 4, -1, -2, 1, 5, -3]
    arr3 = [-3, 1, 2, -3, 4, -1, 5]
    print maxsum(arr3)

if __name__ == '__main__':
    main()
