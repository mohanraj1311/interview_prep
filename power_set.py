set_of_elements = set([1,2,3, 4])
list_of_elements = list(set_of_elements)


print list(set_of_elements)


def powerSet(list_of_elements):
    res = [[]]
    for each_item in sorted(list_of_elements):
        res = res + [[each_item] + each for each in res]
    return res


print powerSet(list_of_elements)


