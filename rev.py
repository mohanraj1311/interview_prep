def rev(s):
    res = []
    s1 = reverse(s)
    words = s1.split(s)
    for each in words:
        res.append(reverse(each))
    s2 = ''.join(res)
    return s2


def reverse(s):

    l = list(s)
    l.reverse()
    return ''.join(l)


def main():
    s = 'the sky is blue'
    print rev(s)


if __name__ == "__main__":
    main()