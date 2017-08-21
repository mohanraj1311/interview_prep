def longest_consecutive_1s(s):
    if len(s) == 0:
        return 0

    lis = list(s)

    x = 1

    curr_count = 0
    prev_count = 0

    for each in lis:

        if int(each) & x == 1:
            curr_count +=1
            if prev_count < curr_count:
                prev_count = curr_count
        else:
            if prev_count < curr_count:
                prev_count = curr_count

            curr_count=0

    print 'result'
    return prev_count


s = '0110111011101111'

print longest_consecutive_1s(s)

