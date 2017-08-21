import copy


def gen_perms(res, temp, A):
    if len(temp) == len(A):
        res.append(copy.copy(temp))
    else:
        for i in xrange(len(A)):
            if A[i] in temp:
                continue
            temp.append(A[i])
            print temp
            gen_perms(res, temp, A)
            temp.pop(len(temp)-1)

def permutaion(A):
    res = []
    temp = []
    gen_perms(res, temp, A)
    return res


print (permutaion([7,3,5]))