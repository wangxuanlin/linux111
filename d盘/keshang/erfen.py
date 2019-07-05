def erfen(l, a):
    j = 0
    i = len(l) -1
    while j <= i:
        k = (i+j) // 2
        if a == l[k]:
            return l[k]
        elif a > l[k]:
            return erfen(l[k+1:],a)
            # j = k + 1
        else:
            return erfen(l[:k], a)
            # i = k - 1





if __name__ == '__main__':
    a = erfen([1, 2, 3, 4, 5, 6, 7], 3)
    print(a)
