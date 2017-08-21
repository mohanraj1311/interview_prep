a = [9, 1, 9]
b = [0, 9, 0]


def add(a, b):
    size_diff = len(a) - len(b)

    for i in xrange(size_diff):
        b.insert(i,0)

    res = [0] * (len(a))
    carry = 0
    i = len(a) - 1
    while(i >= 0):

        res[i] = a[i] + b[i] + carry
        if res[i] > 9:
            carry = res[i] / 10
            res[i] = res[i] % 10
        i = i - 1

    if carry>0:
        return [carry] + res
    else:
        return res


print add(a, b)